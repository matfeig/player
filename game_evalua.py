#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:09:15 2024

@author: matfeig
"""
import pandas as pd
import streamlit as st
import os

# Use an environment variable to specify the path

# csv_file_path = os.getenv('CSV_FILE_PATH', '/Users/matfeig/Desktop/scouting/database.csv')

# df = pd.read_csv(csv_file_path)

csv_file_path = os.getenv('game_eval.csv')

df = pd.read_csv("game_eval.csv")



##########################################################################################

#########################################
# Selecting only the specified columns
selected_columns = ['Date', 'Role de evaluateur', 'Equipe','Nom',
                    'Theme 1 : Efficacite et rendement avec ballon',
                    'Theme 2 : Impact physique',
                    'Theme 3 : Comprehension du jeu ',
                    'Theme 4 : Leadership ',
                    'Theme 5 : Prends le dessus sur adversaire direct',
                    'Theme 6 : Montre sa qualité spéciale  ',
                    'Theme 7 : Implication defensive',
                    'Axe de developpement sur micro-cycle',
                    'Remarques - Agir et penser comme un pro']


df_selected = df[selected_columns]
df_selected = df_selected.loc[:, ~df_selected.columns.duplicated(keep='first')]

df_selected  = df_selected.rename(columns={'Role de evaluateur': 'Evaluateur'})
df_selected  = df_selected.rename(columns={'Theme 1 : Efficacite et rendement avec ballon': 'Efficacité ballon'})
df_selected  = df_selected.rename(columns={'Theme 2 : Impact physique': 'Défis Physique'})
df_selected  = df_selected.rename(columns={'Theme 3 : Comprehension du jeu ': 'Comprehension du jeu'})
df_selected  = df_selected.rename(columns={'Theme 4 : Leadership ': 'Leadership'})
df_selected  = df_selected.rename(columns={'Theme 5 : Prends le dessus sur adversaire direct': 'Relation adv'})
df_selected  = df_selected.rename(columns={'Theme 6 : Montre sa qualité spéciale  ': 'Qualité spéciale'})
df_selected  = df_selected.rename(columns={'Theme 7 : Implication defensive': 'Implication défensive'})
df_selected  = df_selected.rename(columns={'Axe de developpement sur micro-cycle': 'Axe de développement'})
df_selected  = df_selected.rename(columns={'Remarques - Agir et penser comme un pro': 'Act like a Pro'})

selected_col = ['Efficacité ballon',
                'Comprehension du jeu',
                'Leadership',
                'Relation adv',
                'Qualité spéciale',
                'Implication défensive',
                'Défis Physique']


#####

# Calculate the sum of the three selected columns for each row and add it as a new column
df_selected['Note /21'] = df_selected[selected_col].sum(axis=1)



###########################################################################################

# Sélection des colonnes à afficher
select_columns = ['Nom','Note /21','Efficacité ballon', 'Défis Physique', 'Comprehension du jeu','Leadership','Qualité spéciale',
                  'Relation adv','Implication défensive'
                  
                  ]  # Assurez-vous que les noms de colonnes correspondent exactement à ceux de votre fichier CSV

# Filtrer le DataFrame pour ne conserver que les colonnes sélectionnées
filtered_df = df_selected[select_columns]
filtered_df = filtered_df.reset_index(drop=True)
filtered_df = filtered_df.iloc[::-1].reset_index(drop=True)



#################################################################################

# Créer l'interface utilisateur avec Streamlit
st.title('Joueurs Potentiels | Servette FC')


# Filtres
position_options = st.multiselect('Filtrer par Joueur', options=df_selected['Nom'].unique())

# Appliquer les filtres
if position_options:
    filtered_df = filtered_df[filtered_df['Nom'].isin(position_options)]

st.write("Liste des joueurs")
st.table(filtered_df)








