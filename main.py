# main.py - Version interactive avec zones de liste déroulantes (corrigée)

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp
from datetime import datetime

class InsuranceApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Écran principal
        screen = MDScreen()
        
        # Layout principal avec scroll
        scroll = MDScrollView()
        main_box = MDBoxLayout(
            orientation='vertical',
            spacing=dp(20),
            adaptive_height=True,
            padding=dp(20)
        )
        
        # En-tête avec titre
        header_card = MDCard(
            elevation=3,
            padding=dp(20),
            size_hint_y=None,
            height=dp(80),
            md_bg_color=self.theme_cls.primary_color
        )
        
        title = MDLabel(
            text="🚗 CALCULATEUR ASSURANCE AUTOMOBILE",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H5",
            halign="center",
            valign="center"
        )
        header_card.add_widget(title)
        main_box.add_widget(header_card)
        
        # Section 1: Informations véhicule
        info_card = MDCard(
            elevation=2,
            padding=dp(20),
            size_hint_y=None,
            height=dp(520),  # Hauteur augmentée pour 6 champs
            radius=[10, 10, 10, 10]
        )
        
        info_box = MDBoxLayout(
            orientation='vertical',
            spacing=dp(15)
        )
        
        section_title1 = MDLabel(
            text="📋 INFORMATIONS VEHICULE",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height=dp(40)
        )
        info_box.add_widget(section_title1)

                
        # Genre avec bouton dropdown visible
        genre_container = self.create_dropdown_field(
            "Genre de véhicule", 
            "🚙", 
            ["véhicule particulier", "autocar", "camion", "camionnette", 
             "tracteur routier", "engin de chantier", "moto"]
        )
        self.genre_field = genre_container['field']
        self.genre_menu = genre_container['menu']
        info_box.add_widget(genre_container['widget'])
        
        # Puissance
        puissance_container = self.create_dropdown_field(
            "Puissance fiscale",
            "⚡",
            ["1 cv", "2 cv", "3 cv", "4 cv", "5 cv", "6 cv", "7 cv", 
             "8 cv", "9 cv", "10 cv", "11 cv", "12 cv", "plus de 12 cv"]
        )
        self.puissance_field = puissance_container['field']
        self.puissance_menu = puissance_container['menu']
        info_box.add_widget(puissance_container['widget'])
        
        # Énergie
        energie_container = self.create_dropdown_field(
            "Type d'énergie",
            "⛽",
            ["essence", "diesel", "electrique"]
        )
        self.energie_field = energie_container['field']
        self.energie_menu = energie_container['menu']
        info_box.add_widget(energie_container['widget'])
        
        # Usage
        usage_container = self.create_dropdown_field(
            "Usage du véhicule",
            "🎯",
            ["promenades-affaires", "location", "vehicule de société"]
        )
        self.usage_field = usage_container['field']
        self.usage_menu = usage_container['menu']
        info_box.add_widget(usage_container['widget'])
        
        # Formule d'assurance
        formule_container = self.create_dropdown_field(
            "Formule d'assurance",
            "📑",
            ["tiers simple", "tiers intermédiaire", "tous risques"]
        )
        self.formule_field = formule_container['field']
        self.formule_menu = formule_container['menu']
        info_box.add_widget(formule_container['widget'])

        # Durée d'assurance
        duree_container = self.create_dropdown_field(
            "Durée de l'assurance",
            "⏳",
            ["1 mois", "3 mois", "6 mois", "1 an"]
        )
        self.duree_field = duree_container['field']
        self.duree_menu = duree_container['menu']
        info_box.add_widget(duree_container['widget'])
        
        info_card.add_widget(info_box)
        main_box.add_widget(info_card)
           
        # Section 2: Détails techniques
        tech_card = MDCard(
            elevation=2,
            padding=dp(20),
            size_hint_y=None,
            height=dp(280),
            radius=[10, 10, 10, 10]
        )
        
        tech_box = MDBoxLayout(
            orientation='vertical',
            spacing=dp(15)
        )
        
        section_title2 = MDLabel(
            text="🔧 DETAILS TECHNIQUES",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height=dp(40)
        )
        tech_box.add_widget(section_title2)
        
        # Charge utile
        self.charge_field = self.create_input_field("Charge utile (kg)", "📦", 'float')
        tech_box.add_widget(self.charge_field)
        
        # Places assises
        self.places_field = self.create_input_field("Places assises", "👥", 'int')
        tech_box.add_widget(self.places_field)
        
        # Date avec bouton calendrier visible
        date_container = MDRelativeLayout(size_hint_y=None, height=dp(60))
        
        self.date_field = MDTextField(
            hint_text="Date de mise en circulation",
            readonly=True,
            size_hint_y=None,
            height=dp(56),
            line_color_focus=self.theme_cls.primary_color
        )
        
        date_button = MDIconButton(
            icon="calendar",
            theme_icon_color="Custom",
            icon_color=self.theme_cls.primary_color,
            pos_hint={'center_y': 0.5, 'right': 0.95}
        )
        date_button.bind(on_release=self.show_date_picker)
        
        date_container.add_widget(self.date_field)
        date_container.add_widget(date_button)
        tech_box.add_widget(date_container)
        
        tech_card.add_widget(tech_box)
        main_box.add_widget(tech_card)
        
        # Bouton de calcul stylisé
        calc_button = MDRaisedButton(
            text="💰 CALCULER LE DEVIS",
            size_hint_y=None,
            height=dp(60),
            md_bg_color=self.theme_cls.accent_color,
            elevation=5
        )
        calc_button.bind(on_release=self.calculer)
        main_box.add_widget(calc_button)
        
        # Résultat dans une carte avec hauteur adaptative
        self.result_card = MDCard(
            elevation=3,
            padding=dp(20),
            size_hint_y=None,
            height=dp(120),  # Hauteur initiale plus grande
            radius=[10, 10, 10, 10],
            md_bg_color=(0.95, 0.95, 0.95, 1)
        )
        
        self.result_label = MDLabel(
            text="💡 Remplissez les champs ci-dessus pour obtenir un devis personnalisé",
            theme_text_color="Custom",
            text_color=(0, 0.5, 0, 1),
            font_style="Subtitle1",
            text_size=(None, None),  # Permettre le redimensionnement automatique
            halign="left",
            valign="top"
        )
        
        self.result_card.add_widget(self.result_label)
        main_box.add_widget(self.result_card)
        
        scroll.add_widget(main_box)
        screen.add_widget(scroll)
        
        return screen
    
    def create_dropdown_field(self, hint_text, icon, items):
        """Crée un champ avec dropdown visible"""
        container = MDRelativeLayout(size_hint_y=None, height=dp(60))
        
        field = MDTextField(
            hint_text=hint_text,
            readonly=True,
            size_hint_y=None,
            height=dp(56),
            line_color_focus=self.theme_cls.primary_color
        )
        
        # Bouton dropdown visible
        dropdown_button = MDIconButton(
            icon="menu-down",
            theme_icon_color="Custom",
            icon_color=self.theme_cls.primary_color,
            pos_hint={'center_y': 0.5, 'right': 0.95}
        )
        
        # Menu déroulant
        menu = MDDropdownMenu(
            caller=field,
            items=[{"text": f"{icon} {item}", "on_release": lambda x=item: self.set_field(field, x, menu)} 
                   for item in items],
            width_mult=5,
            max_height=dp(200)
        )
        
        dropdown_button.bind(on_release=lambda x: menu.open())
        field.bind(on_focus=lambda instance, value: menu.open() if value else None)
        
        container.add_widget(field)
        container.add_widget(dropdown_button)
        
        return {
            'widget': container,
            'field': field,
            'menu': menu
        }
    
    def create_input_field(self, hint_text, icon, input_filter):
        """Crée un champ de saisie avec icône"""
        container = MDRelativeLayout(size_hint_y=None, height=dp(60))
        
        field = MDTextField(
            hint_text=hint_text,
            input_filter=input_filter,
            size_hint_y=None,
            height=dp(56),
            line_color_focus=self.theme_cls.primary_color
        )
        
        icon_button = MDIconButton(
            icon="pencil" if input_filter else "information",
            theme_icon_color="Custom",
            icon_color=self.theme_cls.primary_color,
            pos_hint={'center_y': 0.5, 'right': 0.95},
            disabled=True
        )
        
        container.add_widget(field)
        container.add_widget(icon_button)
        
        return container
    
    def set_field(self, field, value, menu):
        """Met à jour le champ et ferme le menu"""
        field.text = value
        menu.dismiss()
    
    def show_date_picker(self, *args):
        """Affiche le sélecteur de date"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_date)
        date_dialog.open()
    
    def set_date(self, instance, value, *args):
        """Met à jour le champ date"""
        self.date_field.text = value.strftime('%d/%m/%Y')

    def calculer(self, *args):
        """Calcule le devis d'assurance"""
        try:
            # Récupération des valeurs
            base = 100_000
            genre = self.genre_field.text
            puissance = self.puissance_field.text
            energie = self.energie_field.text
            usage = self.usage_field.text
            formule = self.formule_field.text
            duree = self.duree_field.text

            # Vérification des champs obligatoires
            if not all([genre, puissance, energie, usage, formule, duree]):
                self.result_label.text = "❌ Erreur : Veuillez remplir tous les champs obligatoires"
                self.result_label.text_color = (1, 0, 0, 1)
                self.update_result_size()
                return
            
            # Récupération des valeurs optionnelles
            charge_field_widget = next((child for child in self.charge_field.children if isinstance(child, MDTextField)), None)
            places_field_widget = next((child for child in self.places_field.children if isinstance(child, MDTextField)), None)
            
            charge_text = charge_field_widget.text if charge_field_widget else ""
            places_text = places_field_widget.text if places_field_widget else ""
            date_str = self.date_field.text
            
            # Conversion des valeurs
            charge = float(charge_text) if charge_text else 0
            places = int(places_text) if places_text else 0
            
            if not date_str:
                self.result_label.text = "❌ Erreur : Veuillez sélectionner une date de mise en circulation"
                self.result_label.text_color = (1, 0, 0, 1)
                self.update_result_size()
                return
            
            # Calcul de l'ancienneté
            mise_en_circ = datetime.strptime(date_str, "%d/%m/%Y")
            anciennete = datetime.now().year - mise_en_circ.year
            
            # Application des multiplicateurs
            if genre == "camion":
                base *= 1.5
            if usage == "location":
                base *= 1.3
            if energie == "diesel":
                base *= 1.2
            if puissance == "plus de 12 cv":
                base *= 2.0
            
            # Ajouts fixes
            base += charge * 100
            base += places * 500
            
            # Facteur d'ancienneté
            base *= (1 + (anciennete * 0.02))

            # Ajustement selon la formule d'assurance
            if formule == "tiers intermédiaire":
                base *= 1.2
            elif formule == "tous risques":
                base *= 1.5

            # Ajustement selon la durée d'assurance
            if duree == "3 mois":
                base *= 1.3
            elif duree == "6 mois":
                base *= 1.6
            elif duree == "1 an":
                base *= 2.0
            
            # Construction du texte de résultat
            prix_format = f"{int(base):,}".replace(',', ' ')
            result_text = f"✅ DEVIS ESTIMATIF : {prix_format} FCFA\n\n"
            
            # Ajout d'informations détaillées de manière plus compacte
            result_text += f"📋 DÉTAILS:\n"
            result_text += f"• Genre: {genre}\n"
            result_text += f"• Puissance: {puissance}\n"
            result_text += f"• Énergie: {energie}\n"
            result_text += f"• Usage: {usage}\n"
            result_text += f"• Formule: {formule}\n"
            result_text += f"• Durée: {duree}\n"
            result_text += f"• Ancienneté: {anciennete} ans\n"
            
            if charge > 0:
                result_text += f"• Charge utile: {charge} kg\n"
            if places > 0:
                result_text += f"• Places assises: {places}\n"
            if date_str:
                result_text += f"• Date mise en circulation: {date_str}\n"

            self.result_label.text = result_text
            self.result_label.text_color = (0, 0.7, 0, 1)
            
            # Mise à jour de la taille de la carte de résultat
            self.update_result_size()

        except ValueError:
            self.result_label.text = "❌ Erreur : Veuillez vérifier les valeurs numériques saisies"
            self.result_label.text_color = (1, 0, 0, 1)
            self.update_result_size()
        except Exception as e:
            self.result_label.text = f"❌ Erreur : {str(e)}"
            self.result_label.text_color = (1, 0, 0, 1)
            self.update_result_size()
    
    def update_result_size(self):
        """Met à jour la taille de la carte de résultat selon le contenu"""
        # Calculer approximativement la hauteur nécessaire
        text_lines = self.result_label.text.count('\n') + 1
        # Hauteur approximative : 25dp par ligne + padding
        required_height = max(dp(120), text_lines * dp(25) + dp(40))
        
        # Mettre à jour la hauteur de la carte
        self.result_card.height = required_height
        
        # Configurer le text_size pour permettre le wrapping
        self.result_label.text_size = (self.result_card.width - dp(40), None)

if __name__ == '__main__':
    InsuranceApp().run()