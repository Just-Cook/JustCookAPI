from app_justcook import app, db
from app_justcook.models.item import ItemModel
from app_justcook.models.tecnica import TecnicaModel
from app_justcook.models.modulo import ModuloModel
from app_justcook.models.receita import ReceitaModel
from app_justcook.models.ingrediente import IngredienteModel




def drop_db():
    db.drop_all()

def create_db():
    db.create_all(app=app)
    print("Banco criado.")


'''
    Niveis:
    Muito facil = 1
    Facil = 2
    Intermediário = 3
    Avançado = 4
'''
def populate_db():


    #Tecnica
    tecnica_forno = TecnicaModel(titulo="Como utilizar o forno?", image_name="tecnica_forno")
    db.session.add(tecnica_forno)
    db.session.commit()


    #Item
    item_forno_1 = ItemModel(titulo="Como utilzar o forno?", image_name="tecnica_forno", descricao="""

    Para acender um forno a gás primeiro deve encontrar a chama piloto, localizada no fundo do eletrodoméstico. Só tem que abrir a porta e olhar no seu interior, onde logo no centro se situa uma peça de metal pequena.
    Em seguida, aproxime do buraco do piloto um fósforo ou um isqueiro para acender o forno. Deve aparecer uma chama azul, que indicará que o forno já pode ser utilizado.
    Depois, coloque o eletrodoméstico para funcionar com os botões correspondentes e pronto. Já pode começar a cozinhar!

    O forno a gás atinge mais rapidamente um nível elevado de calor comparado com o forno elétrico, além de esfriar mais depressa depois. Este sistema em sua classe convencional tem pontos quentes e pontos frios, o que faz com que o alimento não cozinhe de forma equilibrada. Para resolver isso é melhor adquirir um forno a gás de convecção, que dispõe de uma ventoinha interior para repartir o calor de forma uniforme. A ventoinha do forno é muito útil para melhorar a circulação de ar, tentando assar os alimentos de forma equitativa. Além disso, também pode ser usada para evitar que a receita saia úmida pela combustão do gás. Assim, a ventoinha mantém o alimento crocante e seco.

    Os fornos a gás também podem chegar a queimar a parte de baixo dos seus alimentos, porque o calor costuma ser muito elevado na parte inferior deste eletrodoméstico. Portanto, para evitar que isso aconteça, é recomendável utilizá-lo com uma bandeja ou panela para cozinhar de forma isolada.

    Neste tipo de fornos, a temperatura costuma ser irregular devido à liberação do gás que varia segundo o momento. Se estiver preocupado por desconhecer a temperatura em que está assando um alimento, o ideal é recorrer a um termômetro de forno, que poderá colocar no centro do mesmo para encontrar o nível de calor do mesmo.
    Quanto a onde colocar os seus alimentos para assar ou cozinhar, para usar um calor mais direto recomenda-se colocar a bandeja na parte de baixo; caso contrário, pode situá-la na parte superior. Por outro lado, mesmo no meio também é uma boa opção se preferir um resultado equilibrado.
    """, tecnica_id=tecnica_forno.id)

    db.session.add(item_forno_1)
    db.session.commit()




    #Tecnica
    tecnica_panela_pressao = TecnicaModel(titulo="Como utilizar a panela de pressão?", image_name="tecnica-panela-pressao")
    db.session.add(tecnica_panela_pressao)
    db.session.commit()

    #Item
    item_panela_pressao_1 = ItemModel(titulo="Como utilizar a panela de pressão?", image_name="tecnica-panela-pressao",
    descricao= """
        A primeira coisa para se observar ao usar a panela de pressão é que dentro dela tem uma marca de nível máximo.
        Isso quer dizer que você só vai encher a panela até aquele nível. Se não tiver aquela marca, só encha 2/3 da panela.

        1. Coloque o alimento dentro da panela. Nunca coloque alimentos muito secos, use líquidos (água) para que a panela funcione perfeitamente e evite acidentes.
        2. Tampe a panela tomando o cuidado que a borracha da tampa esteja bem colocada.
        3. Leve ao fogo alto até ferver.
        4. Quando o pino começar a chiar e a balançar, abaixe o fogo.
        5. Depois que o tempo de cozimento passar desligue a panela e espere esfriar para sair toda a pressão de dentro antes de abrir. NUNCA ABRA A PANELA SEM RETIRAR A PRESSÃO.
        6. Se quiser tirar a pressão mais rapidamente, tire a panela do fogo, deixe esfriar um pouco e depois coloque embaixo da torneira molhando apenas a lateral da panela.
        7. Se o pino abaixou e não faz mais barulho quando você toca nele, então toda a pressão saiu e você pode abrir a panela.
        """, tecnica_id=tecnica_panela_pressao.id)

    db.session.add(item_panela_pressao_1)
    db.session.commit()




    item_panela_pressao_2 = ItemModel(titulo="Cuidados que você deve ter", image_name=None, descricao="""
        Nunca abra a panela sem ter certeza que não tem mais pressão dentro dela.
        Só compre panelas de pressão com selo do Inmetro, não compre panelas de ambulantes.
        Se o chiar do pino parar enquanto a panela estiver fervendo desligue o fogo, a panela não está funcionando corretamente.
        Depois de usar a panela lave muito bem todas as partes, inclusive o pino e a borracha.
        Se você observar que a borracha está seca ou querendo se partir, troque imediatamente.
        Última coisa, panela de pressão não é eterna (isso é só uma marca) então, se verificar algum problema ou a panela já está velhinha mesmo, não tenha dúvida, troque.
    """, tecnica_id=tecnica_panela_pressao.id)

    db.session.add(item_panela_pressao_2)
    db.session.commit()



    #Tecnica
    tecnica_maminha = TecnicaModel(titulo="O que é maminha?", image_name="tecnica-maminha")
    db.session.add(tecnica_maminha)
    db.session.commit()


    #Item

    item_maminha_1 = ItemModel(titulo="O que é maminha?", image_name="tecnica_maminha", descricao="""
        A Maminha está entre os cortes bovinos considerados nobres. É um corte de carne muito procurado  para churrasco, pois é oriunda da peça completa de alcatra, que é composta ainda pelo miolo da alcatra e pela picanha.
        Ou seja, erroneamente acredita-se que a Maminha é retirada da alcatra, mas apesar de ser ligada por uma membrana, não se trata do mesmo músculo.
        É localizada no fim da peça inteira da alcatra (“rabo da alcatra”), próxima à ponta da agulha, no traseiro do boi.

        É considerada uma carne muito macia (quando cortada contra as fibras), suculenta, de sabor suave, que contém gordura. Deve ser cortada de forma correta, ou seja, contra as fibras, para acentuar sua maciez e sabor.
        Se o corte das suas fibras for feito longitudinalmente, acompanhando o corte do miolo da alcatra por exemplo, torna-se uma carne dura.
    """, tecnica_id=tecnica_maminha.id)

    db.session.add(item_maminha_1)
    db.session.commit()



    item_maminha_2 = ItemModel(titulo="Dicas e curiosidades",  image_name=None, descricao="""
        Uma peça de maminha pesa, em média, 2kg.
        A maminha tem uma pequena diferença em relação ao miolo da alcatra. Suas fibras são em forma de leque e o corte deve ser feito contra as fibras, em leque mesmo, mas isso compromete, de certa forma, as pontas.
        Na Argentina, esse corte é bem mais aproveitado que no Brasil, pois neste tem sido vendido juntamente com o miolo de alcatra e não separado.
        Uma alternativa para que a maminha seja uma carne mais valorizada, é colocar o corte em bandejas, ou em embalagem a vácuo, agregando valor ao corte, que é ótima opção para um bom churrasco.
        Sempre que possível asse-a com sua própria gordura para que a carne permaneça suculenta e macia e não perca sua umidade natural e nutrientes.
        Pode assar envolta em papel alumínio ou celofane.
        Por sua localização atende pelos nomes de ponta de alcatra ou Colita de Cuadril (em espanhol), Aiguillette Baronne (em francês) e Tail of round ou Tri-tip (em inglês).
    """, tecnica_id=tecnica_maminha.id)

    db.session.add(item_maminha_2)
    db.session.commit()


    item_maminha_3 = ItemModel(titulo="Características Nutricionais", image_name=None, descricao="""
        Água   75%
        Proteína   21%
        Sais minerais   3%
        Gordura   2%
        Vitaminas   0,03%
    """, tecnica_id=tecnica_maminha.id)

    db.session.add(item_maminha_3)
    db.session.commit()




    #Tecnica
    tecnica_carne = TecnicaModel(titulo="Manipulação e higiene da carne bovina", image_name="tecnica-carne-bovina")
    db.session.add(tecnica_carne)
    db.session.commit()



    #Item

    item_carne_1 = ItemModel(titulo="Manipulação e higiene da carne bovina", image_name="tecnica-carne-bovina",
    descricao="""
        A carne bovina é um alimento extremamente rico em proteínas, vitaminas, sais minerais e elevado teor de umidade.
        Estas características da carne a tornam um produto propício ao desenvolvimento de microrganismos, caso ela não seja conservada adequadamente e manipulada em condições rígidas de limpeza do local e do próprio manipulador.

        Para uma boa conservação da carne em casa são necessários cuidados rigorosos para evitar alterações e contaminações. Assim, deve-se sempre obedecer a limites de tempo e temperatura, que são utilizados nos vários métodos de conservação.
        Quando se fala de carnes frescas, os meios de conservação são os que usam frio, como refrigeração e o congelamento. A refrigeração deve ser o método adotado para a carne que será preparada e consumida em até 72h após a compra.
        No caso de período maior deve-se optar pelo congelamento. Se congelada, a carne deverá passar por um período de descongelamento para o seu preparo. Este processo também requer técnicas e cuidados essenciais para se manter a qualidade e a integridade do alimento.

        Para garantir a qualidade da carne e a segurança alimentar de seus consumidores, é importante estar atento a alguns conselhos básicos de higiene, que devem virar rotina em toda prática culinária:

        1. Lavar bem as mãos e fazê-lo constantemente: as mãos devem ser lavadas antes do preparo de alimentos e novamente após interrupções (como ir ao banheiro, manipular utensílios sujos, mexer no cabelo ou tocar em cestos de lixo).
        Não se deve lidar com quaisquer alimentos após a manipulação de alimentos crus (como as carnes) sem antes lavar novamente as mãos. Lembre-se também de que unhas compridas podem abrigar microrganismos, servindo de foco de contaminação;
        2. Lavar as superfícies e utensílios que entrarão em contato com a carne: a higienização deve ser feita com água (preferencialmente quente) e sabão. Devem ser lavadas as tábuas, as facas, os martelos, as vasilhas, assim como a pia e quaisquer outras superfícies;
        3. Não usar utensílios que já tiverem sido utilizados com carnes cruas para outros alimentos sem antes lavá-los bem com água e sabão;
        4. Não se deve falar, cantar ou tossir sobre os alimentos;
        5. É importante não colocar as mãos no nariz, na boca ou nos cabelos durante o preparo dos alimentos;
        6. Não se deve enxugar as mãos em panos ou em aventais antes de manusear carnes;
        7. Não se deve lidar com dinheiro enquanto se trabalha com alimentos;
        8. Convém usar, de preferência, roupas limpas;
        9. Os cabelos devem estar presos ou contidos por uma rede durante o preparo das refeições;
        10. Os alimentos não devem ser manipulados por pessoas que estiverem com doenças de pele, diarréia, gripe, dor de garganta ou doenças infecciosas;
        11. A cozinha deve ser mantida limpa e os utensílios devem estar sempre lavados. Não se esqueça de usar detergentes e desinfetantes;
        12. A geladeira e o freezer não devem ficar superlotados, pois isso dificulta a circulação de ar frio dentro do aparelho e compromete a conservação dos alimentos;
        13. Mantenha o lixo em recipiente limpo, revestido de saco plástico e sempre tampado, evitando assim o aparecimento de insetos, baratas e ratos;
        14. Se possível, evite o uso de utensílios de madeira, como tábuas de carne e martelos de amaciar, pois a madeira é um material poroso, que absorve muito líquidos e é de difícil higienização, o que favorece a multiplicação de microrganismos. Tais objetos podem tornar-se focos de contaminação dos alimentos. Prefira utensílios plásticos ou de aço inoxidável, que, além de serem mais resistentes ao tempo, são de fácil limpeza.
    """, tecnica_id=tecnica_carne.id)


    db.session.add(item_carne_1)
    db.session.commit()


    #Modulo
    modulo_almoco_domingo = ModuloModel(titulo="Fazer a mamãe feliz", subtitulo="Almoço de domingo",image_name="modulo-almoco-domingo",
    descricao="Nesse módulo você irá aprender algumas receitas que irão deixar o seu almoço de domingo muito mais saboroso.", nivel=2)

    modulo_almoco_domingo.tecnicas.append(tecnica_forno)
    modulo_almoco_domingo.tecnicas.append(tecnica_maminha)
    modulo_almoco_domingo.tecnicas.append(tecnica_panela_pressao)
    modulo_almoco_domingo.tecnicas.append(tecnica_carne)

    db.session.add(modulo_almoco_domingo)
    db.session.commit()


    #Receita
    receita_maminha = ReceitaModel(titulo="Maminha assada na crosta de sal",
    descricao="A maminha é um corte muito suculento e saboroso, sempre uma boa opção para os almoços com os amigos e a família.",
    image_name="receita-maminha", rendimento=10, tempo=5400, modulo_id=modulo_almoco_domingo.id)

    db.session.add(receita_maminha)
    db.session.commit()

    receita_feijao_verde = ReceitaModel(titulo="Feijão verde cremoso",
    descricao="Com baixas calorias e sem colesterol, o feijão verde é um alimento precioso da gastronomia nordestina. Os grãos deliciosos e crocantes ainda são ricos em vitamina, cálcio e ferro. Já é o suficiente para te convencer a experimentar essa receita, certo?",
    image_name="receita-feijao-verde", rendimento=8, tempo=900, modulo_id=modulo_almoco_domingo.id)

    db.session.add(receita_feijao_verde)
    db.session.commit()

    receita_arroz_brocolis = ReceitaModel(titulo="Arroz de brócolis", descricao="Ricos em fibras, ácido fólico, vitamina C, ferro, cálcio e magnésio, os brócolis vão muito bem com massas! Então que tal unir todas essas qualidades com o nosso queridinho arroz branco?",
    image_name="receita-arroz-brocolis", rendimento=8, tempo=1800, modulo_id=modulo_almoco_domingo.id)

    db.session.add(receita_arroz_brocolis)
    db.session.commit()


    #Ingrediente

    ingrediente_maminha_1 = IngredienteModel(nome="peça de maminha", quantidade=1, unidade=None,
    receita_id=receita_maminha.id)

    db.session.add(ingrediente_maminha_1)
    db.session.commit()

    ingrediente_maminha_2 = IngredienteModel(nome="sal grosso", quantidade=1, unidade="Kg",
    receita_id=receita_maminha.id)

    db.session.add(ingrediente_maminha_2)
    db.session.commit()

    ingrediente_feijao_verde_1 = IngredienteModel(nome="feijão verde", quantidade=500, unidade="gramas",
    receita_id = receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_1)
    db.session.commit()


    ingrediente_feijao_verde_2 = IngredienteModel(nome="tablete de caldo de galinha", quantidade=1, unidade=None,
    receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_2)
    db.session.commit()

    ingrediente_feijao_verde_3 = IngredienteModel(nome="cebola", quantidade=1, unidade=None, receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_3)
    db.session.commit()

    ingrediente_feijao_verde_4 = IngredienteModel(nome="dente de alho", quantidade=4, unidade=None, receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_4)
    db.session.commit()

    ingrediente_feijao_verde_5 = IngredienteModel(nome="requeijão", quantidade=1, unidade="copo", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_5)
    db.session.commit()

    ingrediente_feijao_verde_6 = IngredienteModel(nome="queijo coalho", quantidade=100, unidade="gramas", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_6)
    db.session.commit()

    ingrediente_feijao_verde_7 = IngredienteModel(nome="creme de leite", quantidade=1, unidade="caixa", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_7)
    db.session.commit()

    ingrediente_feijao_verde_8 = IngredienteModel(nome="azeite de oliva", quantidade=2, unidade="colher de sopa", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_8)
    db.session.commit()

    ingrediente_feijao_verde_9 = IngredienteModel(nome="cheiro verde", quantidade=None, unidade="a gosto", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_9)
    db.session.commit()

    ingrediente_arroz_brocolis_1 = IngredienteModel(nome="arroz branco", quantidade=3, unidade="xícaras", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_1)
    db.session.commit()

    ingrediente_arroz_brocolis_2 = IngredienteModel(nome="dente de alho", quantidade=3, unidade=None, receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_2)
    db.session.commit()

    ingrediente_arroz_brocolis_3 = IngredienteModel(nome="óleo", quantidade=2, unidade='colher de sopa', receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_3)
    db.session.commit()

    ingrediente_arroz_brocolis_4 = IngredienteModel(nome="água", quantidade=4, unidade="xícaras", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_4)
    db.session.commit()

    ingrediente_arroz_brocolis_5 = IngredienteModel(nome="brócolis", quantidade=1, unidade=None, receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_5)
    db.session.commit()

    ingrediente_arroz_brocolis_6 = IngredienteModel(nome="azeite", quantidade=2, unidade="colher de sopa", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_6)
    db.session.commit()

    ingrediente_arroz_brocolis_7 = IngredienteModel(nome="sal", quantidade=None, unidade="a gosto", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_7)
    db.session.commit()
