import plotly.graph_objects as go
import plotly.offline as pyo

atributes = ['Attack', 'Agility', 'Magic Defence',
             'Magic Attack', 'Defence']
atributes = [*atributes, atributes[0]]

paladin_1 = [35, 25, 23, 18, 23]
mage_2 = [15, 15, 30, 30, 18]
archer_3 = [23, 35, 15, 15, 23]
paladin_1 = [*paladin_1, paladin_1[0]]
mage_2 = [*mage_2, mage_2[0]]
archer_3 = [*archer_3, archer_3[0]]

party = go.Figure(
    data=[
        go.Scatterpolar(r=paladin_1, theta=atributes, name='Ikki'),
        go.Scatterpolar(r=mage_2, theta=atributes, name='Ikki'),
        go.Scatterpolar(r=archer_3, theta=atributes, name='Ikki')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Rpg Game group comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(party)
