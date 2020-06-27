from app_justcook import app, db
from app_justcook.models.item import ItemModel
from app_justcook.models.tecnica import TecnicaModel
from app_justcook.models.modulo import ModuloModel
from app_justcook.models.receita import ReceitaModel
from app_justcook.models.ingrediente import IngredienteModel
from app_justcook.models.passo import PassoModel
from app_justcook.models.dica import DicaModel




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
    item_forno_1 = ItemModel(titulo="Como utilzar o forno?", image_name="tecnica_forno", descricao="""Para acender um forno a gás primeiro deve encontrar a chama piloto, localizada no fundo do eletrodoméstico. Só tem que abrir a porta e olhar no seu interior, onde logo no centro se situa uma peça de metal pequena.

Em seguida, aproxime do buraco do piloto um fósforo ou um isqueiro para acender o forno. Deve aparecer uma chama azul, que indicará que o forno já pode ser utilizado. Depois, coloque o eletrodoméstico para funcionar com os botões correspondentes e pronto. Já pode começar a cozinhar!

O forno a gás atinge mais rapidamente um nível elevado de calor comparado com o forno elétrico, além de esfriar mais depressa depois. Este sistema em sua classe convencional tem pontos quentes e pontos frios, o que faz com que o alimento não cozinhe de forma equilibrada. Para resolver isso é melhor adquirir um forno a gás de convecção, que dispõe de uma ventoinha interior para repartir o calor de forma uniforme. A ventoinha do forno é muito útil para melhorar a circulação de ar, tentando assar os alimentos de forma equitativa. Além disso, também pode ser usada para evitar que a receita saia úmida pela combustão do gás. Assim, a ventoinha mantém o alimento crocante e seco.

Os fornos a gás também podem chegar a queimar a parte de baixo dos seus alimentos, porque o calor costuma ser muito elevado na parte inferior deste eletrodoméstico. Portanto, para evitar que isso aconteça, é recomendável utilizá-lo com uma bandeja ou panela para cozinhar de forma isolada.

Neste tipo de fornos, a temperatura costuma ser irregular devido à liberação do gás que varia segundo o momento. Se estiver preocupado por desconhecer a temperatura em que está assando um alimento, o ideal é recorrer a um termômetro de forno, que poderá colocar no centro do mesmo para encontrar o nível de calor do mesmo.

Quanto a onde colocar os seus alimentos para assar ou cozinhar, para usar um calor mais direto recomenda-se colocar a bandeja na parte de baixo; caso contrário, pode situá-la na parte superior. Por outro lado, mesmo no meio também é uma boa opção se preferir um resultado equilibrado.""",
    tecnica_id=tecnica_forno.id)

    db.session.add(item_forno_1)
    db.session.commit()




    #Tecnica
    tecnica_panela_pressao = TecnicaModel(titulo="Como utilizar a panela de pressão?", image_name="tecnica-panela-pressao")
    db.session.add(tecnica_panela_pressao)
    db.session.commit()

    #Item
    item_panela_pressao_1 = ItemModel(titulo="Como utilizar a panela de pressão?", image_name="tecnica-panela-pressao",
    descricao= """A primeira coisa para se observar ao usar a panela de pressão é que dentro dela tem uma marca de nível máximo.
Isso quer dizer que você só vai encher a panela até aquele nível. Se não tiver aquela marca, só encha 2/3 da panela.

1. Coloque o alimento dentro da panela. Nunca coloque alimentos muito secos, use líquidos (água) para que a panela funcione perfeitamente e evite acidentes.
2. Tampe a panela tomando o cuidado que a borracha da tampa esteja bem colocada.
3. Leve ao fogo alto até ferver.
4. Quando o pino começar a chiar e a balançar, abaixe o fogo.
5. Depois que o tempo de cozimento passar desligue a panela e espere esfriar para sair toda a pressão de dentro antes de abrir. NUNCA ABRA A PANELA SEM RETIRAR A PRESSÃO.
6. Se quiser tirar a pressão mais rapidamente, tire a panela do fogo, deixe esfriar um pouco e depois coloque embaixo da torneira molhando apenas a lateral da panela.
7. Se o pino abaixou e não faz mais barulho quando você toca nele, então toda a pressão saiu e você pode abrir a panela.""",
    tecnica_id=tecnica_panela_pressao.id)

    db.session.add(item_panela_pressao_1)
    db.session.commit()




    item_panela_pressao_2 = ItemModel(titulo="Cuidados que você deve ter", image_name=None, descricao="""Nunca abra a panela sem ter certeza que não tem mais pressão dentro dela. Só compre panelas de pressão com selo do Inmetro, não compre panelas de ambulantes.

Se o chiar do pino parar enquanto a panela estiver fervendo desligue o fogo, a panela não está funcionando corretamente. Depois de usar a panela lave muito bem todas as partes, inclusive o pino e a borracha. Se você observar que a borracha está seca ou querendo se partir, troque imediatamente.

Última coisa, panela de pressão não é eterna (isso é só uma marca) então, se verificar algum problema ou a panela já está velhinha mesmo, não tenha dúvida, troque.
    """, tecnica_id=tecnica_panela_pressao.id)

    db.session.add(item_panela_pressao_2)
    db.session.commit()



    #Tecnica
    tecnica_maminha = TecnicaModel(titulo="O que é maminha?", image_name="tecnica-maminha")
    db.session.add(tecnica_maminha)
    db.session.commit()


    #Item

    item_maminha_1 = ItemModel(titulo="O que é maminha?", image_name="tecnica_maminha", descricao="""A Maminha está entre os cortes bovinos considerados nobres. É um corte de carne muito procurado  para churrasco, pois é oriunda da peça completa de alcatra, que é composta ainda pelo miolo da alcatra e pela picanha. Ou seja, erroneamente acredita-se que a Maminha é retirada da alcatra, mas apesar de ser ligada por uma membrana, não se trata do mesmo músculo. É localizada no fim da peça inteira da alcatra (“rabo da alcatra”), próxima à ponta da agulha, no traseiro do boi.

É considerada uma carne muito macia (quando cortada contra as fibras), suculenta, de sabor suave, que contém gordura. Deve ser cortada de forma correta, ou seja, contra as fibras, para acentuar sua maciez e sabor. Se o corte das suas fibras for feito longitudinalmente, acompanhando o corte do miolo da alcatra por exemplo, torna-se uma carne dura.
    """, tecnica_id=tecnica_maminha.id)

    db.session.add(item_maminha_1)
    db.session.commit()



    item_maminha_2 = ItemModel(titulo="Dicas e curiosidades",  image_name=None, descricao="""Uma peça de maminha pesa, em média, 2kg. A maminha tem uma pequena diferença em relação ao miolo da alcatra. Suas fibras são em forma de leque e o corte deve ser feito contra as fibras, em leque mesmo, mas isso compromete, de certa forma, as pontas. Na Argentina, esse corte é bem mais aproveitado que no Brasil, pois neste tem sido vendido juntamente com o miolo de alcatra e não separado.

Uma alternativa para que a maminha seja uma carne mais valorizada, é colocar o corte em bandejas, ou em embalagem a vácuo, agregando valor ao corte, que é ótima opção para um bom churrasco. Sempre que possível asse-a com sua própria gordura para que a carne permaneça suculenta e macia e não perca sua umidade natural e nutrientes. Pode assar envolta em papel alumínio ou celofane.

Por sua localização atende pelos nomes de ponta de alcatra ou Colita de Cuadril (em espanhol), Aiguillette Baronne (em francês) e Tail of round ou Tri-tip (em inglês).
    """, tecnica_id=tecnica_maminha.id)

    db.session.add(item_maminha_2)
    db.session.commit()


    item_maminha_3 = ItemModel(titulo="Características Nutricionais", image_name=None, descricao="""Água   75%
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
    descricao="""A carne bovina é um alimento extremamente rico em proteínas, vitaminas, sais minerais e elevado teor de umidade. Estas características da carne a tornam um produto propício ao desenvolvimento de microrganismos, caso ela não seja conservada adequadamente e manipulada em condições rígidas de limpeza do local e do próprio manipulador.

Para uma boa conservação da carne em casa são necessários cuidados rigorosos para evitar alterações e contaminações. Assim, deve-se sempre obedecer a limites de tempo e temperatura, que são utilizados nos vários métodos de conservação. Quando se fala de carnes frescas, os meios de conservação são os que usam frio, como refrigeração e o congelamento. A refrigeração deve ser o método adotado para a carne que será preparada e consumida em até 72h após a compra. No caso de período maior deve-se optar pelo congelamento. Se congelada, a carne deverá passar por um período de descongelamento para o seu preparo. Este processo também requer técnicas e cuidados essenciais para se manter a qualidade e a integridade do alimento.

Para garantir a qualidade da carne e a segurança alimentar de seus consumidores, é importante estar atento a alguns conselhos básicos de higiene, que devem virar rotina em toda prática culinária:

1. Lavar bem as mãos e fazê-lo constantemente: as mãos devem ser lavadas antes do preparo de alimentos e novamente após interrupções (como ir ao banheiro, manipular utensílios sujos, mexer no cabelo ou tocar em cestos de lixo). Não se deve lidar com quaisquer alimentos após a manipulação de alimentos crus (como as carnes) sem antes lavar novamente as mãos. Lembre-se também de que unhas compridas podem abrigar microrganismos, servindo de foco de contaminação;
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


    tecnica_ovo = TecnicaModel(titulo="Como quebrar um ovo?", image_name="tecnica-ovo")
    db.session.add(tecnica_ovo)
    db.session.commit()


    item_ovo_1 = ItemModel(titulo="Como quebrar um ovo?", image_name="tecnica-ovo", descricao="""Pegue o ovo com a mão dominante. Faça isso com firmeza de modo que a lateral dele fique voltada para baixo. Bata, com cuidado, uma mesma parte do ovo em uma superfície plana até a casca começar a ceder. Depois, pressione seu polegar contra a parte da casca que cedeu para abrir o ovo.

Remova qualquer fragmento de casca que cair no ovo. Mesmo que você tenha dominado a técnica de quebrar ovos, algumas cascas ainda podem ficar na clara e na gema. Para resolver o problema, molhe os dedos e use-os para pegar as cascas. Dessa forma, a água deve atrair naturalmente os pedaços de casca aderidos no ovo.
    """, tecnica_id=tecnica_ovo.id)

    db.session.add(item_ovo_1)
    db.session.commit()

    tecnica_medidas = TecnicaModel(titulo="Medidas", image_name="tecnica-medidas")
    db.session.add(tecnica_medidas)
    db.session.commit()

    item_medidas_1 = ItemModel(titulo="Medidas", image_name="tecnica-medidas", descricao="""Se você está começando a se aventurar agora na cozinha, provavelmente já se deparou com medidas que te deixaram confuso. Afinal, quanto é uma pitada? um punhado?

Como, geralmente, as receitas citam base de medida que podem ter tamanhos bastante variados, o correto é usar medidores padronizados, que são facilmente encontrados em lojas de artigos de cozinha. Com os medidores, você terá menos problemas colocando uma quantidade diferente da necessária.
    """, tecnica_id = tecnica_medidas.id)

    db.session.add(item_medidas_1)
    db.session.commit()

    item_medida_2 = ItemModel(titulo="Temos algumas dicas pra você se preparar", image_name=None, descricao="""1. Meça condimentos em qualquer lugar que não seja sobre a tigela em que estão os outros ingredientes, porque se você errar vai estragar tudinho!
2. Afofe e peneire ingredientes secos como farinhas, açúcar e outros, antes de serem medidos. Coloque-os cuidadosamente no recipiente de medida, sem comprimi-los.
3. Coloque o recipiente para medir ingredientes líquidos sobre uma superfície reta e verifique o nível na altura da vista.
4. Retire da Geladeira com antecedência as gorduras sólidas como manteigas, margarinas, banhas e outras, para que sejam medidas na temperatura ambiente. Coloque no recipiente de medida, apertando para que não fiquem buracos vazios ou bolhas de ar.
    """, tecnica_id = tecnica_medidas.id)

    db.session.add(item_medida_2)
    db.session.commit()

    item_medida_3 = ItemModel(titulo="Agora algumas medidas que você pode tomar como base", image_name=None, descricao="""1. Uma pitada quer dizer pegar um pouquinho do ingrediente na ponta dos dedos juntando o polegar e o indicador; o que ficar entre os dois dedos é a pitada ou 1/2 colher (chá). Experimente se com a pitada sua receita ficou boa. Geralmente a pitada é a gosto principalmente no caso do sal.
2. Um punhado quer dizer encher a mão com o ingrediente que vai ser usado e fechá-la; o que ficar na sua mão é o punhado.
3. uma porção de macarrão basta usar o buraco no meio da colher de macarrão para medir ainda cru.
4. fio é quando traçamos uma linha, fazemos um risco com o ingrediente.

Lembrando que estes números são valores aproximados, pois cada ingrediente tem um peso diferente, e a quantidade varia conforme a massa de cada um. Portanto, o ideal mesmo é ter o medidor. Utilize essas medidas apenas como base, e em último caso, utilize uma lata ou caixa vazia (de creme de leite, ou milho) para medir, pegando como medida a quantidade descrita no rótulo.
    """, tecnica_id = tecnica_medidas.id)

    db.session.add(item_medida_3)
    db.session.commit()

    tecnica_panelas = TecnicaModel(titulo="Tipos de Panelas", image_name="tecnica-panelas")
    db.session.add(tecnica_panelas)
    db.session.commit()

    item_panela_1 = ItemModel(titulo="Tipos de Panelas", image_name="tecnica-panelas", descricao="""Existem diferentes tipos de panelas e cada um traz características únicas para o preparo das suas receitas. Na hora de preparar nossas receitas favoritas, as panelas são itens essenciais e que fazem toda a diferença. Entretanto, o que muita gente não sabe é que existem diferentes tipos de panelas e cada uma delas, traz características únicas, que podem influenciar no preparo dos alimentos.
    """, tecnica_id=tecnica_panelas.id)

    db.session.add(item_panela_1)
    db.session.commit()

    item_panela_2 = ItemModel(titulo="Panelas de alumínio", image_name="tecnica-panelas-aluminio", descricao="""Talvez um dos modelos mais conhecidos, as panelas de alumínio são conhecidas por serem leves e resistentes. Dentre os tipos de panela, elas são ideais para preparar doces, frituras e refogados. Também são boas para manter o sabor dos alimentos, mesmo quando eles são submetidos à altas temperaturas. Esse tipo de panela é uma opção para fritura de alimentos por imersão, pois mantém uma boa qualidade do óleo que pode ser utilizado por mais de uma vez.

Ao contrário do que se pensa, alimentos fritos com mais óleo, e posteriormente colocados sobre papel absorvente, retém menos óleo do que os fritos em pouca quantidade.

Não polir ou usar abrasivos internamente, pois isso evita que o material contamine os alimentos.
    """, tecnica_id=tecnica_panelas.id)

    db.session.add(item_panela_2)
    db.session.commit()

    item_panela_3 = ItemModel(titulo="Panela Teflon (revestimento antiaderente)", image_name="tecnica-panelas-teflon", descricao="""Este tipo de panela recebe um revestimento de antiaderentes, o que evita que os alimentos grudem.

Ela é ótima para qualquer tipo de preparo, mas precisa de alguns cuidados, como a lavagem com esponjas macias e o uso de utensílios de plastico ou silicone, para evitar riscos e danos.""",
     tecnica_id = tecnica_panelas.id)

    db.session.add(item_panela_3)
    db.session.commit()

    item_panela_4 = ItemModel(titulo="Panela de Aço Inox", image_name="tecnica-panelas-aco", descricao="""Com alta durabilidade e excelente qualidade, as panelas de aço inox são ótimas para várias preparações na cozinha, incluindo aquelas que precisam ser cozidas por muito tempo.

Mesmo assim, este tipo de panela requer cuidados, tanto na hora de lavar quanto na conservação, pois elas tendem a escurecer se não forem bem secas. Uma desvantagem é o fato de não serem ideais para frituras, pois esquentam muito rápido e tendem a queimar os alimentos quando imersos em óleo.
    """, tecnica_id=tecnica_panelas.id)

    db.session.add(item_panela_4)
    db.session.commit()

    tecnica_utensilios = TecnicaModel(titulo="Utensílios", image_name="tecnica-utensilio")
    db.session.add(tecnica_utensilios)
    db.session.commit()

    item_utensilio_1 = ItemModel(titulo="Utensilios", image_name="tecnica-utensilio", descricao="""Para ser funcional, uma cozinha não precisa ser muito grande, mas é indispensável que ela seja bem equipada.

Assim, será mais fácil tornar seu dia a dia prático e fazer com que os preparos dos alimentos sejam mais rápidos, simples e adequados. Até lá, é de suma importância contar com o básico, que lhe permitirá realizar uma série de preparos e serví-los adequadamente.

Sem esses itens, dificilmente você conseguirá realizar as receitas mais triviais. Por isso, é ideal ter acessórios como as espátulas, que são ideais pra mexer ingredientes quentes e frios, além de serem ótimas pra servir patês, manteigas e muito mais! Vem comigo ver mais sobre elas!
    """, tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_1)
    db.session.commit()

    item_utensilio_2 = ItemModel(titulo="Espátula de silicone", image_name=None, descricao="""As espátulas de silicone são incríveis pra qualquer tipo de alimento, além de não danificarem nenhum recipiente! O silicone ainda é fácil de lavar e bem flexível, viu?

E sabe o que é mais legal? O silicone não transfere calor, ou seja, mesmo que você esteja cozinhando em alta temperatura, o cabo da espátula não esquenta! Quer mais? Uma espátula desse tipo suporta temperaturas de até 220°C!
    """, tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_2)
    db.session.commit()

    item_utensilio_3 = ItemModel(titulo="Espátula pra manteiga ou patê", image_name=None, descricao="""Olha, pra quem quer deixar a hora do café ou lanche da tarde perfeito, pode escolher uma espátula de inox pra passar manteiga, geleias, patês e muito mais!

Gente, esse modelo fica incrível na decoração da sua mesa e ainda arrasa na forma de servir, pois é bem resistente até pra passar manteigas mais duras, viu?
    """, tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_3)
    db.session.commit()

    item_utensilio_4 = ItemModel(titulo="Espátula com furos", image_name=None, descricao="""Pra quem prepara alimentos que precisam ser fritos, a espátula com furos é o acessório ideal! O modelo vem com aberturas pro óleo escorrer e, ao mesmo tempo, você ainda consegue pegar o alimento pra colocar em outro recipiente, além de poder mexer na própria panela.

Legal, né? Tem espátulas que são feitas de nylon, um material super-resistente em altas temperaturas!""",
     tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_4)
    db.session.commit()

    item_utensilio_5 = ItemModel(titulo="Espátula reta", image_name=None, descricao="""Ideal pra cortar pizzas e mexer em ingredientes que vão na chapa, a espátula reta é um dos modelos mais legais que existem, né? Sem contar que ela corta muito bem, além de ser fácil de lavar! Se você é daqueles que amam preparar refeições na chapa, aposte nesta espátula!""",
     tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_5)
    db.session.commit()

    item_utensilio_6 = ItemModel(titulo="Espátula com dobra pra bolo", image_name=None, descricao="""Outra tarefa pra espátula é passar coberturas em um bolo, além de também fatiar. Gente, a espátula com dobra é incrível, pois ajuda a cortar melhor, sem erros, e ainda passa, por exemplo, aquela cobertura de chocolate em cima do bolo! Adorei!""",
     tecnica_id=tecnica_utensilios.id)

    db.session.add(item_utensilio_6)
    db.session.commit()

    item_utensilio_7 = ItemModel(titulo="Espátula pra torta", image_name=None, descricao="""Cortar uma torta nunca mais será a mesma coisa depois que você usar uma espátula! É incrível como ela corta massas de tortas e ajuda você a tirar fatias sem quebrar, legal, né? Um dos melhores modelos são os feitos em aço inox, fáceis de lavar, duram bastante e ainda são higiênicos.""",
     tecnica_id = tecnica_utensilios.id)

    db.session.add(item_utensilio_7)
    db.session.commit()


    tecnica_acucar = TecnicaModel(titulo="Açúcar cristal x Açúcar mascavo", image_name="tecnica-acucar")

    db.session.add(tecnica_acucar)
    db.session.commit()

    item_acucar_1 = ItemModel(titulo="Os tipos de açúcar", image_name="tecnica-tipos-acucar", descricao="""A regra básica é a seguinte: quanto mais escuro é o açúcar, mais vitaminas e sais minerais ele tem, e mais perto do estado bruto ele está.

A cor branca significa que o açúcar recebeu aditivos químicos no último processo da fabricação, o refinamento, que a gente explica direitinho no fim do texto. Apesar de esses aditivos deixarem o produto bonitão, eles também “roubam” a maioria dos nutrientes.

Só para dar um exemplo, em 100 gramas de um açúcar bem escuro, o mascavo, existem 85 miligramas de cálcio, 29 miligramas de magnésio, 22 miligramas de fósforo e 346 miligramas de potássio.

Para comparar, na mesma quantidade de açúcar refinado, aquele tipo branco mais comum, a gente encontra no máximo 2 miligramas de cada um desses nutrientes.""",
    tecnica_id=tecnica_acucar.id)

    db.session.add(item_acucar_1)
    db.session.commit()

    item_acucar_2 = ItemModel(titulo="O processo", image_name=None, descricao= """A matéria-prima do nosso açúcar, você sabe, é a cana. Antes de chegar à nossa mesa, a planta passa por diversas etapas de fabricação.

Primeiro, ela é moída para extrair o caldo doce. Depois, começa a purificação, em que o caldo é aquecido a 105 ºC e filtrado para barrar as impurezas. Em seguida, o caldo é evaporado, vira um xarope e segue para o cozimento, onde aparecem os cristais de açúcar que a gente conhece.

Por último, os tipos mais brancos de açúcar ainda passam pelo refinamento, quando o produto recebe tratamentos químicos para melhorar seu gosto e seu aspecto. O resultado final é o açúcar em cristais, mas, se você moldar e comprimir os cristais com xarope de açúcar, dá para fabricar açúcar em torrões.

Além da cana, há açúcar nas frutas e no milho (a frutose) e no leite (a lactose). A beterraba é outra fonte de açúcar, mas tem um processo de extração diferente. Ela é popular na Europa: como lá não tem cana, a beterraba entrou na dança. """,
    tecnica_id=tecnica_acucar.id)

    db.session.add(item_acucar_2)
    db.session.commit()


    tecnica_frituras = TecnicaModel(titulo="Frituras", image_name="tecnica-frituras")

    db.session.add(tecnica_frituras)
    db.session.commit()

    item_frituras_1 = ItemModel(titulo="O processo de fritura", image_name="tecninca-fritura", descricao="""Na fritura, observa-se um processo simultâneo de transferência de calor e de massa: o calor é transferido do óleo para o alimento; a água que evapora do alimento é absorvida pelo óleo. Assim, os fatores que afetam a transferência de calor e da massa afetam as propriedades térmicas e físico-químicas do óleo e do alimento.

O processo de fritura é realizado em recipientes abertos,à temperatura elevada (180 – 200°C), em contato direto com o ar. A fritura é um processo apropriado aos vegetais ricos em amido, como é o caso das batatas e mandioca. Pela brusca imersão em gordura quente, o amido forma uma crosta impermeável que retém em seu interior o vapor de água.

No entanto, deve ser evitado o aquecimento em excesso, pois no caso dos vegetais ocorre a caramelização dos açúcares e os produtos adquirem um sabor amargo e pouco agradável.""",
    tecnica_id=tecnica_frituras.id)

    db.session.add(item_frituras_1)
    db.session.commit()

    item_fritura_2 = ItemModel(titulo="Tipos de fritura", image_name=None, descricao="""Fritura superficial – ocorre em frigideiras e recipientes de pouca profundidade, sendo que o alimento fica parcialmente na gordura quente;

Fritura de imersão – o alimento fica totalmente em óleo quente.""", tecnica_id= tecnica_frituras.id)

    db.session.add(item_fritura_2)
    db.session.commit()

    item_fritura_3 = ItemModel(titulo="Pré-preparo", image_name=None, descricao="""Antes de fritar qualquer tipo de alimento que se queria, é necessário realizar um pré-preparo.

Geralmente cada tipo de alimento consiste em um tipo de pré preparo como verifica-se a seguir:

Enfarinhar – consiste em proteger o alimento com uma ligeira camada de farinha, muito comum em pescados;
Encapado – o alimento é recoberto com massa de ovo, massa de trigo, leite, ervas, à milanesa (farinha-ovo-farinha);
Empanado – operação em que o alimento é recoberto com pão ralado (farinha de rosca) antes da fritura.

O oléo que é usado para a fritura desempenha uma dupla função: de um lado, atua como meio de transferência de calor, e por outro lado, pode ser absorvido pelo alimento, integrando-se ao mesmo como ingrediente.""",
    tecnica_id=tecnica_frituras.id)

    db.session.add(item_fritura_3)
    db.session.commit()


    tecnica_banana = TecnicaModel(titulo="Como comprar bananas?", image_name="tenica-comprar-banana")

    db.session.add(tecnica_banana)
    db.session.commit()

    item_banana_1 = ItemModel(titulo="Como escolher?", image_name="tecnica-comprar-banana", descricao="""Na hora de escolher a fruta é preciso observar a presença de manchas escuras: quanto maiores, mais madura estará a fruta que, em alguns casos, pode estar passada.

O ideal é comprar frutas firmes, livre de partes moles ou machucados, e com casca amarela e pequenas manchas. Se não for para consumo imediato, dê preferência às que estão apenas ligeiramente verdes.""",
    tecnica_id=tecnica_banana.id)

    db.session.add(item_banana_1)
    db.session.commit()

    item_banana_2 = ItemModel(titulo="Armazenamento", image_name=None, descricao="As bananas amadurecem aos poucos. Devem ser conservadas em local seco e fresco e não dentro da geladeira. À temperatura ambiente, a banana se conserva por 4 dias.",
    tecnica_id=tecnica_banana.id)

    db.session.add(item_banana_2)
    db.session.commit()

    item_banana_3 = ItemModel(titulo="Consumo", image_name=None, descricao="É a variedade que contém mais fibras e amido, por isto é consumida na forma cozida ou assada no preparo de purês e cremes.",
    tecnica_id = tecnica_banana.id)

    db.session.add(item_banana_3)
    db.session.commit()

    tecnica_iorgute = TecnicaModel(titulo="Beneficios do Iogurte Natural", image_name="tecnica-iogurte-natural-small")

    db.session.add(tecnica_iorgute)
    db.session.commit()

    item_iorgute_1 = ItemModel(titulo="Iogurte Natural", image_name="tecnica-iogurte-natural-big", descricao="""O iogurte é um alimento apreciado por pessoas das mais diversas idades, sendo assim uma excelente opção para incrementar as refeições.

Além de ser um alimento muito saboroso, é também extremamente benéfico para o nosso organismo, pois é uma importante fonte de: proteínas, carboidratos, gorduras, vitaminas (A, B1, B2, B3, B6, B12, C, D), potássio, cálcio, fósforo, magnésio, zinco, ferro, sódio, biotina, ácido pantotênico, ácido fólico, colina e inositol.

Sendo assim, listamos nesta matéria os principais benefícios do consumo de iogurte natural e ensinamos como fazer o iogurte natural caseiro, com uma receita simples e prática. Confira.""",
    tecnica_id=tecnica_iorgute.id)

    db.session.add(item_iorgute_1)
    db.session.commit()

    item_iorgute_2 = ItemModel(titulo="Benefícios do Iorgute Natural", image_name=None, descricao="""O maior benefício que o consumo de iogurte proporciona ao nosso organismo é a ação dos lactobacilos probióticos presentes nele. Os lactobacilos são organismos vivos que auxiliam o corpo na digestão dos alimentos, sintetização das vitaminas e processamento dos hormônios.

Além disso, o consumo dos lactobacilos vivos ajuda na prevenção e no tratamento de doenças como infecções vaginais até outras mais sérias como úlcera e câncer do intestino.

O iogurte também é uma excelente opção para quem sofre de intolerância à lactose. Como os lactobacilos acidificam todo o açúcar natural do leite – a lactose – mesmo quem sofre com o problema pode consumir o produto à vontade.

Segundo uma pesquisa recente do Departamento de Bioquímica do Instituto de Biologia da UERJ, o iogurte também ajuda a diminuir a quantidade de nitritos no organismo, responsáveis pela formação das nitrosaminas. E considerando que as nitrosaminas podem provocar câncer de estômago e esôfago a ingestão de lactobacilos se torna ainda mais importante.

Porém, para se beneficiar totalmente da ingestão dos lactobacilos, é importante consumir o iogurte o mais próximo possível da sua data de fabricação. Isso se deve ao fato de que os lactobacilos diminuem com o passar do tempo.""",
    tecnica_id=tecnica_iorgute.id)

    db.session.add(item_iorgute_2)
    db.session.commit()

    item_iorgute_3 = ItemModel(titulo="Impacto do consumo de iorgute no organismo", image_name=None, descricao="""Incluir o iogurte na sua alimentação diária pode contribuir nos seguintes aspectos:

- Bom funcionamento do intestino e combate às bactérias presentes nele, promovendo a limpeza do local;

- Aumento dos níveis de cálcio no organismo, ajudando no combate à osteoporose e mantendo os ossos e dentes mais fortes;

- Bom funcionamento do sistema de absorção de nutrientes;

- Restauração da flora bacteriana, livre de efeitos colaterais;

- Diminuição da fermentação, dos gases, das flatulências, das inflamações e das infecções intestinais;

- Melhoria do sistema imunológico;

- Renovação dos tecidos do corpo;

- Desaceleração do processo de envelhecimento;

- Melhoria na queima de gorduras e diminuição da barriga;

- Reposição do cálcio no período da menopausa.""",
    tecnica_id=tecnica_iorgute.id)

    db.session.add(item_iorgute_3)
    db.session.commit()

    tecnica_frango = TecnicaModel(titulo="Beneficios do Frango", image_name="tecnica-benficios-frango-small")

    db.session.add(tecnica_frango)
    db.session.commit()

    item_frango_1 = ItemModel(titulo="Beneficios do Frago", image_name="tecnica-benficios-frango-big", descricao="""Existem várias razões para o frango ser tão conhecido, entre elas ser uma boa fonte de proteína magra com nutrientes essenciais, como vitaminas, minerais e aminoácidos.

A carne de frango é indicada para quem está de dieta por possuir uma quantidade de gorduras saturadas muito menor do que a carne bovina. Veja a seguir seis benefícios que a carne de frango traz para a saúde:

1- Proteção contra o câncer
O frango é rico em niacina (vitamina B3), essencial para a proteção contra o câncer. Uma pequena porção de carne de frango podem atender as necessidades de niacina para o dia inteiro. O selênio presente na carne de frango também ajuda na proteção contra a doença.

2- Benefícios para o cérebro
A niacina contida na carne de frango também é essencial para a saúde do cérebro e pode ter efeitos protetores contra o Mal de Alzheimer.

3- Faz bem para o coração
A vitamina B6 do frango mantém a saúde do coração em dia. Além disso, a carne de frango ajuda a manter os níveis de homocisteína baixos. Os altos níveis dessa substância podem causar danos às paredes dos vasos sanguíneos.

4- Tireoide
O selênio na carne de frango ajuda a manter a função da tireoide. Um estudo descobriu que a deficiência ou baixos níveis de selênio podem levar a problemas nesta glândula.

5- Arma contra a obesidade
A carne de frango é uma ótima opção para quem está tentando perder peso. O frango contém pouca gordura e menos calorias do que outras carnes, como as carnes bovina e suína. Além disso, é uma excelente fonte de proteínas.

6- Frango é energia
O frango aumenta a energia do corpo graças às vitaminas B6 e B3. Se você está sentindo um pouco de cansaço ou desgastado, tente comer carne de frango para dar impulso de nutrientes, como vitaminas e minerais. As calorias presentes nesta carne auxiliam no aumento dos níveis de energia.""",
    tecnica_id=tecnica_frango.id)

    db.session.add(item_frango_1)
    db.session.commit()

    tecnica_gluten = TecnicaModel(titulo="Conhece o Glúten?", image_name="tenica-gluten-small")

    db.session.add(tecnica_gluten)
    db.session.commit()

    item_gluten_1 = ItemModel(titulo="Conhece o Glúten?", image_name="tecnica-gluten-big", descricao="""O glúten é uma mistura de duas proteínas, gliadina e glutenina, ambas presentes no trigo, cevada, centeio e aveia. A função do ingrediente é deixar a massa mais macia e elástica e, ao mesmo tempo, mais resistente para que não se arrebente ao ser puxada.

Ele também tem a função de auxiliar no crescimento do alimento, porque forma uma rede protetora após o processo de sovar, que impede o escape do gás carbônico formado durante a fase de fermentação.

Dito isso, como a substância é presente em pães, massas, torradas, bolos, biscoitos e até cerveja, consumimos glúten com bastante frequência. Apesar de ser uma ótima fonte de energia para as atividades diárias e para regular o intestino, o glúten, como aponta a nutricionista Cintya Bassi, do Hospital e Maternidade São Cristóvão, pode provocar uma série de malefícios para quem é celíaco.

A doença celíaca tem origem genética e é autoimune, ou seja, consiste em uma falha do sistema de defesa do nosso organismo que faz com que ele ataque a si mesmo. O portador da doença celíaca não pode ingerir glúten, já que este inflama a mucosa intestinal e prejudica o desempenho do corpo na absorção de nutrientes, gerando sintomas tanto no intestino como fora dele, explica Flávia Cyfer, nutricionista do Espaço Longevitá, no Rio.

Entre os problemas associados à doença celíaca e o consumo de glúten estão a diarreia crônica ou constipação, anemia, falta de apetite, vômito, emagrecimento ou obesidade, atraso no crescimento, alteração de humor, distensão e dor abdominal, aftas de repetição. Todavia, quem não é celíaco mas apresenta hipersensibilidade ao glúten pode sentir sintomas parecidos.

A diferença fica por conta apenas das vilosidades do intestino, que não serão danificadas e na inexistência de uma doença crônica, frisa Cintya.

A associação que muitas pessoas fazem do glúten com inchaço no corpo não está errada. “A retenção de líquidos muitas vezes é sinal de intoxicação. Ao retirar a ‘toxina’, ele desincha. Melhora muito”, explicou Flávia. De toda forma, abrir mão do glúten na dieta não garante que você irá emagrecer.

De acordo com Cintya, é possível que a exclusão do glúten da dieta resulte em perda de peso, mas não porque o glúten engorda e sim porque a proteína está presente em diversos alimentos comuns, e, muitas vezes, calóricos.

“O inchaço, especialmente abdominal, é uma queixa muito comum e normalmente suas causas estão relacionadas a má digestão ou constipação”, explica Cintya. Alimentos que formam gases também podem causar inchaço, além de laticínios, açúcar refinado, bebidas gaseificadas e alimentos ricos em sódio.

Para evitar esse problema, a médica sugere optar por uma alimentação equilibrada, sem excesso dos alimentos citados, priorizando alimentos integrais, frutas, verduras e legumes, e uma hidratação reforçada.

O substituto mais comum do glúten é a farinha de arroz, que pode ser utilizada em receitas de pão, bolo e torta. Outra opção é usar povilho ou fécula de batata no lugar da proteína. Glúten também pode ser substituído por farinha de trigo sarraceno; biomassa de banana verde, que tem demonstrado benefícios no controle do colesterol de acordo com Cintya; farinha de coco, especialmente em bolos e tortas; e quinoa em flocos, para o preparo de bolos e biscoitos.

Para levar uma vida mais saudável, experimente trocar o trigo por arroz integral, quinoa, amaranto ou arroz negro. Abrir mão do pão e substituir por batata doce, baroa, inhame ou aipim também traz resultados mais saudáveis.

“A ideia é trocar por 'alimento' sem glúten em vez de biscoitinhos e industrializados sem glúten, mas nada saudáveis”, reforça Flávia.""",
    tecnica_id=tecnica_gluten.id)

    db.session.add(item_gluten_1)
    db.session.commit()



    #Modulo

    modulo_culinaria_basica = ModuloModel(titulo="O Começo de uma Aventura", subtitulo="Culinária Básica", image_name="modulo-culinaria-basica",
    descricao="Nesse módulos você aprenderá receitas básicas pra sobreviver na cozinha", nivel=1)

    modulo_culinaria_basica.tecnicas.append(tecnica_ovo)
    modulo_culinaria_basica.tecnicas.append(tecnica_medidas)
    modulo_culinaria_basica.tecnicas.append(tecnica_panelas)
    modulo_culinaria_basica.tecnicas.append(tecnica_utensilios)

    db.session.add(modulo_culinaria_basica)
    db.session.commit()


    modulo_culinaria_literaria = ModuloModel(titulo="Que gostinho doce", subtitulo="Culinária Literária", image_name="modulo-culinaria-literaria",
    descricao="Nesse módulo você irá aprender algumas receitas que apareceram em livros famosos e com certeza você já ouviu falar sobre.", nivel=2)

    modulo_culinaria_literaria.tecnicas.append(tecnica_panelas)
    modulo_culinaria_literaria.tecnicas.append(tecnica_acucar)
    modulo_culinaria_literaria.tecnicas.append(tecnica_frituras)

    db.session.add(modulo_culinaria_literaria)
    db.session.commit()


    modulo_barato_saudavel = ModuloModel(titulo="Barato e Saudável", subtitulo="Comer bem sem gastar muito", image_name="modulo-barato-saudavel",
    descricao="Nesse modulo você aprender técnicas, dicas e receitas que vão te ajudar a cozinhar de forma saudável e sem gastar muito.", nivel=2)

    modulo_barato_saudavel.tecnicas.append(tecnica_banana)
    modulo_barato_saudavel.tecnicas.append(tecnica_frango)
    modulo_barato_saudavel.tecnicas.append(tecnica_gluten)
    modulo_barato_saudavel.tecnicas.append(tecnica_iorgute)

    db.session.add(modulo_barato_saudavel)
    db.session.commit()

    modulo_almoco_domingo = ModuloModel(titulo="Fazer a mamãe feliz", subtitulo="Almoço de domingo",image_name="modulo-almoco-domingo",
    descricao="Nesse módulo você irá aprender algumas receitas que irão deixar o seu almoço de domingo muito mais saboroso.", nivel=3)

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


    receita_ovo = ReceitaModel(titulo="Ovo frito", descricao="Depois disso, ninguém poderá dizer que você não sabe nem fritar um ovo.", image_name="receita-ovo",
    rendimento=1, tempo=120, modulo_id=modulo_culinaria_basica.id)

    db.session.add(receita_ovo)
    db.session.commit()

    receita_macarrao = ReceitaModel(titulo="Macarrão com calabresa", descricao="O almoço versátil, rápido e simples", image_name="receita-macarrao",
    rendimento=3, tempo=1200, modulo_id=modulo_culinaria_basica.id)

    db.session.add(receita_macarrao)
    db.session.commit()


    receita_cerveja = ReceitaModel(titulo="Cerveja Amanteigada", descricao="LUMOS! Famosa entre os bruxos e elfos domésticos de Hogwarts hoje você vai aprender a fazer cerveja amanteigada. Apesar do nome nessa receita não vamos utilizar cerveja ou álcool.",
    image_name="cerveja-amanteigada", rendimento=10, tempo=1800, modulo_id=modulo_culinaria_literaria.id)

    db.session.add(receita_cerveja)
    db.session.commit()

    receita_bolinho_chuva = ReceitaModel(titulo="Bolinho de chuva", descricao="Marmelada de banana, bananada de goiaba. Goiabada de marmelo. Sítio do Pica-Pau Amarelo! Você já deve ter ouvido falar dos bolinhos de chuva da tia Nastácia, então vou lá!",
    image_name="bolinho-chuva", rendimento=30, tempo=2100, modulo_id=modulo_culinaria_literaria.id)

    db.session.add(receita_bolinho_chuva)
    db.session.commit()

    receita_panqueca = ReceitaModel(titulo="Panqueca de Aveia e Banana", descricao="Aprenda a fazer panquecas fofas e leves para você iniciar bem o seu dia, a começar pelo café da manhã.",
    image_name="panqueca-aveia-banana", rendimento=6, tempo=5400, modulo_id=modulo_barato_saudavel.id)

    db.session.add(receita_panqueca)
    db.session.commit()

    receita_frango = ReceitaModel(titulo="Peito de frango recheado", descricao="Frango é um ingrediente muito versátil, mas tem dias que a cabeça não sabe mais o que inventar pra variar o cardápio da família, né não? E frango grelhado não, por favor não! Porém, inove e aprenda a fazer um frango recheado simples e gostoso.",
    image_name="frango-recheado", rendimento=2, tempo=1800, modulo_id=modulo_barato_saudavel.id)

    db.session.add(receita_frango)
    db.session.commit()

    receita_biscoito_fit = ReceitaModel(titulo="Biscoito fit de banana", descricao="Uma receitinha ultra mega simples, fácil e rápida de preparar, e que pode ser consumida sem culpa alguma já que não leva nem gordura, nem açúcar, nem glúten e nem leite. Isto quer dizer que pode ser consumida por todos, inclusive por diabéticos e pessoas intolerantes ao glúten e à lactose.",
    image_name="biscoito-fit-banana", rendimento=12, tempo=2400,  modulo_id=modulo_barato_saudavel.id)

    db.session.add(receita_biscoito_fit)
    db.session.commit()

    receita_salada = ReceitaModel(titulo="Salada de forno", descricao="Esta salada serve bem umas 4 pessoas e não dá trabalho nenhum: é cortar, arrumar no refratário, investir nos temperinhos e deixar o forno trabalhar pra você.",
    image_name="salada-forno", rendimento=4, tempo=2400, modulo_id=modulo_barato_saudavel.id)

    db.session.add(receita_salada)
    db.session.commit()





    #Ingrediente

    ingrediente_maminha_1 = IngredienteModel(nome="peça de maminha", quantidade=1, unidade="un",
    receita_id=receita_maminha.id)

    db.session.add(ingrediente_maminha_1)
    db.session.commit()

    ingrediente_maminha_2 = IngredienteModel(nome="sal grosso", quantidade=1, unidade="Kg",
    receita_id=receita_maminha.id)

    db.session.add(ingrediente_maminha_2)
    db.session.commit()

    ingrediente_feijao_verde_1 = IngredienteModel(nome="feijão verde", quantidade=500, unidade="g",
    receita_id = receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_1)
    db.session.commit()


    ingrediente_feijao_verde_2 = IngredienteModel(nome="tablete de caldo de galinha", quantidade=1, unidade="un",
    receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_2)
    db.session.commit()

    ingrediente_feijao_verde_3 = IngredienteModel(nome="cebola", quantidade=1, unidade="un", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_3)
    db.session.commit()

    ingrediente_feijao_verde_4 = IngredienteModel(nome="dente de alho", quantidade=4, unidade="un", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_4)
    db.session.commit()

    ingrediente_feijao_verde_5 = IngredienteModel(nome="requeijão", quantidade=1, unidade="copo", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_5)
    db.session.commit()

    ingrediente_feijao_verde_6 = IngredienteModel(nome="queijo coalho", quantidade=100, unidade="g", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_6)
    db.session.commit()

    ingrediente_feijao_verde_7 = IngredienteModel(nome="creme de leite", quantidade=1, unidade="cx", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_7)
    db.session.commit()

    ingrediente_feijao_verde_8 = IngredienteModel(nome="azeite de oliva", quantidade=2, unidade="col. sopa", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_8)
    db.session.commit()

    ingrediente_feijao_verde_9 = IngredienteModel(nome="cheiro verde", quantidade=None, unidade="a gosto", receita_id=receita_feijao_verde.id)

    db.session.add(ingrediente_feijao_verde_9)
    db.session.commit()

    ingrediente_arroz_brocolis_1 = IngredienteModel(nome="arroz branco", quantidade=3, unidade="xíc", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_1)
    db.session.commit()

    ingrediente_arroz_brocolis_2 = IngredienteModel(nome="dente de alho", quantidade=3, unidade="un", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_2)
    db.session.commit()

    ingrediente_arroz_brocolis_3 = IngredienteModel(nome="óleo", quantidade=2, unidade='col. sopa', receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_3)
    db.session.commit()

    ingrediente_arroz_brocolis_4 = IngredienteModel(nome="água", quantidade=4, unidade="xíc", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_4)
    db.session.commit()

    ingrediente_arroz_brocolis_5 = IngredienteModel(nome="brócolis", quantidade=1, unidade="un", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_5)
    db.session.commit()

    ingrediente_arroz_brocolis_6 = IngredienteModel(nome="azeite", quantidade=2, unidade="col. sopa", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_6)
    db.session.commit()

    ingrediente_arroz_brocolis_7 = IngredienteModel(nome="sal", quantidade=None, unidade="a gosto", receita_id=receita_arroz_brocolis.id)

    db.session.add(ingrediente_arroz_brocolis_7)
    db.session.commit()

    ingrediente_ovo_1 = IngredienteModel(nome="ovo", quantidade=1, unidade="un", receita_id = receita_ovo.id)

    db.session.add(ingrediente_ovo_1)
    db.session.commit()

    ingrediente_ovo_2 = IngredienteModel(nome="azeite ou óleo", quantidade=1, unidade="col. chá", receita_id=receita_ovo.id)

    db.session.add(ingrediente_ovo_2)
    db.session.commit()

    ingrediente_ovo_3 = IngredienteModel(nome="sal", quantidade=1, unidade="pitada", receita_id=receita_ovo.id)

    db.session.add(ingrediente_ovo_3)
    db.session.commit()

    ingrediente_ovo_4 = IngredienteModel(nome="pimenta do reino (opcional)", quantidade=1, unidade="pitada", receita_id= receita_ovo.id)

    db.session.add(ingrediente_ovo_4)
    db.session.commit()

    ingrediente_macarrao_1 = IngredienteModel(nome="macarrão espaguete", quantidade=0.5, unidade="pct", receita_id= receita_macarrao.id)

    db.session.add(ingrediente_macarrao_1)
    db.session.commit()

    ingrediente_macarrao_2 = IngredienteModel(nome="água", quantidade=1, unidade="litro", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_2)
    db.session.commit()

    ingrediente_macarrao_3 = IngredienteModel(nome="calabresa", quantidade=1, unidade="un", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_3)
    db.session.commit()

    ingrediente_macarrao_4 = IngredienteModel(nome="queijo ralado", quantidade=5, unidade="col", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_4)
    db.session.commit()

    ingrediente_macarrao_5 = IngredienteModel(nome="molho de tomate", quantidade=1, unidade = "sachê", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_5)
    db.session.commit()

    ingrediente_macarrao_6 = IngredienteModel(nome="cebola", quantidade=0.5, unidade="un", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_6)
    db.session.commit()

    ingrediente_macarrao_7 = IngredienteModel(nome="pimenta do reino", quantidade=1, unidade="pitada", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_7)
    db.session.commit()

    ingrediente_macarrao_8 = IngredienteModel(nome="sal", quantidade=1, unidade="col. chá", receita_id=receita_macarrao.id)

    db.session.add(ingrediente_macarrao_8)
    db.session.commit()

    ingrediente_macarrao_9 = IngredienteModel(nome="azeite ou óleo", quantidade=3, unidade="col. chá", receita_id= receita_macarrao.id )

    db.session.add(ingrediente_macarrao_9)
    db.session.commit()


    ingrediente_cerveja_1 = IngredienteModel(nome="açúcar mascavo", quantidade=0.5, unidade="xíc", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_1)
    db.session.commit()

    ingrediente_cerveja_2 = IngredienteModel(nome="Água", quantidade=2, unidade="col. sopa", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_2)
    db.session.commit()

    ingrediente_cerveja_3 = IngredienteModel(nome="manteiga", quantidade=5, unidade="col. sopa", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_3)
    db.session.commit()

    ingrediente_cerveja_4 = IngredienteModel(nome="limão", quantidade=1, unidade="un", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_4)
    db.session.commit()

    ingrediente_cerveja_5 = IngredienteModel(nome="sal", quantidade=1, unidade="pitada", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_5)
    db.session.commit()

    ingrediente_cerveja_6 = IngredienteModel(nome="essência de baunilha", quantidade=1, unidade="col. chá", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_6)
    db.session.commit()

    ingrediente_cerveja_7 = IngredienteModel(nome="Nata ou creme de leite", quantidade=0.25, unidade="xíc", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_7)
    db.session.commit()

    ingrediente_cerveja_8 = IngredienteModel(nome="água com gás", quantidade=1, unidade="un", receita_id=receita_cerveja.id)

    db.session.add(ingrediente_cerveja_8)
    db.session.commit()

    ingrediente_bolinho_chuva_1 = IngredienteModel(nome="açúcar", quantidade=1, unidade="xíc", receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_1)
    db.session.commit()

    ingrediente_bolinho_chuva_2 = IngredienteModel(nome="ovo", quantidade=2, unidade="un", receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_2)
    db.session.commit()

    ingrediente_bolinho_chuva_3 = IngredienteModel(nome="leite", quantidade=1, unidade="xic", receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_3)
    db.session.commit()

    ingrediente_bolinho_chuva_4 = IngredienteModel(nome="farinha de trigo", quantidade=2.5, unidade="xic", receita_id=receita_bolinho_chuva.id )


    db.session.add(ingrediente_bolinho_chuva_4)
    db.session.commit()

    ingrediente_bolinho_chuva_5 = IngredienteModel(nome="fermento em pó", quantidade=1, unidade="col. sopa", receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_5)
    db.session.commit()

    ingrediente_bolinho_chuva_6 = IngredienteModel(nome="canela em pó", quantidade=1, unidade="col. sopa", receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_6)
    db.session.commit()

    ingrediente_bolinho_chuva_7 = IngredienteModel(nome="óleo", quantidade=None, unidade=None, receita_id=receita_bolinho_chuva.id)

    db.session.add(ingrediente_bolinho_chuva_7)
    db.session.commit()


    ingrediente_banana_1 = IngredienteModel(nome="banana madura", quantidade=1, unidade="un", receita_id=receita_panqueca.id)

    db.session.add(ingrediente_banana_1)
    db.session.commit()

    ingrediente_banana_2 = IngredienteModel(nome="farinha de aveia integral", quantidade=1, unidade="xic", receita_id=receita_panqueca.id)

    db.session.add(ingrediente_banana_2)
    db.session.commit()

    ingrediente_banana_3 = IngredienteModel(nome="bicarbonato de Sódio", quantidade=1, unidade="col. café", receita_id=receita_panqueca.id)

    db.session.add(ingrediente_banana_3)
    db.session.commit()

    ingrediente_banana_4 = IngredienteModel(nome="geleia de arroz ou mel", quantidade=2, unidade="col. sopa", receita_id=receita_panqueca.id)

    db.session.add(ingrediente_banana_4)
    db.session.commit()

    ingrediente_banana_5 = IngredienteModel(nome="iogurte natural", quantidade=1, unidade="un",receita_id=receita_panqueca.id )

    db.session.add(ingrediente_banana_5)
    db.session.commit()

    ingrediente_banana_6 = IngredienteModel(nome="ovo", quantidade=1, unidade="un", receita_id=receita_panqueca.id)

    db.session.add(ingrediente_banana_6)
    db.session.commit()


    ingrediente_frango_1 = IngredienteModel(nome="peito de frango", quantidade=1, unidade="un", receita_id = receita_frango.id)

    db.session.add(ingrediente_frango_1)
    db.session.commit()

    ingrediente_frango_2 = IngredienteModel(nome="sal", quantidade=None, unidade="a gosto", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_2)
    db.session.commit()

    ingrediente_frango_3 = IngredienteModel(nome="pimenta", quantidade=None, unidade="a gosto", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_3)
    db.session.commit()

    ingrediente_frango_4 = IngredienteModel(nome="requeijão", quantidade=2, unidade="col. sopa", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_4)
    db.session.commit()

    ingrediente_frango_5 = IngredienteModel(nome="tomate", quantidade=0.5, unidade="un", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_5)
    db.session.commit()

    ingrediente_frango_6 = IngredienteModel(nome="orégano", quantidade=None, unidade="a gosto", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_6)
    db.session.commit()

    ingrediente_frango_7 = IngredienteModel(nome="molho de tomate", quantidade=0.5, unidade="xic", receita_id=receita_frango.id)

    db.session.add(ingrediente_frango_7)
    db.session.commit()

    ingrediente_biscoito_1 = IngredienteModel(nome="banana nanica", quantidade=2, unidade="un", receita_id=receita_biscoito_fit.id)

    db.session.add(ingrediente_biscoito_1)
    db.session.commit()

    ingrediente_biscoito_2 = IngredienteModel(nome="quinua em flocos", quantidade=1, unidade="xic", receita_id=receita_biscoito_fit.id)

    db.session.add(ingrediente_biscoito_2)
    db.session.commit()

    ingrediente_biscoito_3 = IngredienteModel(nome="canela em pó", quantidade=1, unidade="col. chá", receita_id=receita_biscoito_fit.id)

    db.session.add(ingrediente_biscoito_3)
    db.session.commit()


    ingrediente_salada_1 = IngredienteModel(nome="berinjela", quantidade=2, unidade="un", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_1)
    db.session.commit()


    ingrediente_salada_2 = IngredienteModel(nome="abobrinha", quantidade=1, unidade="xic", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_2)
    db.session.commit()

    ingrediente_salada_3 = IngredienteModel(nome="tomate", quantidade=1, unidade="un", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_3)
    db.session.commit()

    ingrediente_salada_4 = IngredienteModel(nome="azeitona", quantidade=None, unidade="a gosto", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_4)
    db.session.commit()

    ingrediente_salada_5 = IngredienteModel(nome="sal", quantidade=None, unidade="a gosto", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_5)
    db.session.commit()

    ingrediente_salada_6 = IngredienteModel(nome="pimenta", quantidade=None, unidade="a gosto", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_6)
    db.session.commit()

    ingrediente_salada_7 = IngredienteModel(nome="ervas", quantidade=None, unidade="a gosto", receita_id=receita_salada.id)

    db.session.add(ingrediente_salada_7)
    db.session.commit()

    #Passos

    maminha_passo_1 = PassoModel(image_name="maminha-passo-1", descricao="Limpe a maminha retirando o excesso de pele.",
    cronometro=None, dica= "Ligue o forno para aquece-lo 180 graus.",receita_id=receita_maminha.id)
    maminha_passo_1.tecnicas.append(tecnica_maminha)
    maminha_passo_1.tecnicas.append(tecnica_carne)

    db.session.add(maminha_passo_1)
    db.session.commit()

#    maminha_dica_1 = DicaModel(descricao="Ligue o forno para aquece-lo 180 graus.", passo_id=maminha_passo_1.id)

#    db.session.add(maminha_dica_1)

    maminha_passo_2 = PassoModel(image_name="maminha-passo-2", descricao=" Forre uma forma com sal grosso, fazendo uma cama para a maminha e em seguida coloque-a com a gordura virada para cima.",
    cronometro=None,dica="A forma a ser utilizada pode ser de qualquer material que pode ser levado ao forno.", receita_id=receita_maminha.id)

    db.session.add(maminha_passo_2)
    db.session.commit()

#    maminha_dica_2 = DicaModel(descricao="A forma a ser utilizada pode ser de qualquer material que pode ser levado ao forno.",
#    passo_id=maminha_passo_2.id)

#    db.session.add(maminha_dica_2)
#    db.session.commit()

    maminha_passo_3 = PassoModel(image_name="maminha-passo-3", descricao="Cubra o restante da carne com sal grosso, de forma que não fique nenhum pedaço da carne visível.",
    cronometro=None, dica = None, receita_id=receita_maminha.id)

    db.session.add(maminha_passo_3)
    db.session.commit()

    maminha_passo_4 = PassoModel(image_name="maminha-passo-4", descricao=" Leve ao forno para assar em forno pré aquecido a 180 graus por aproximadamente 1h e 30min.",
    cronometro=5400,dica=None, receita_id=receita_maminha.id)
    maminha_passo_4.tecnicas.append(tecnica_forno)

    db.session.add(maminha_passo_4)
    db.session.commit()

    maminha_passo_5 = PassoModel(image_name="maminha-passo-5", descricao="Retire do forno e tire toda a crosta de sal com cuidado",
    cronometro=None, dica=None, receita_id=receita_maminha.id)

    db.session.add(maminha_passo_5)
    db.session.commit()

    maminha_passo_6 = PassoModel(image_name="maminha-passo-6", descricao="Leve a carne a uma tábua de corte para fatiá-la e monte em uma travessa sem desmontar a peça.",
    cronometro=None, dica = None, receita_id=receita_maminha.id)

    db.session.add(maminha_passo_6)
    db.session.commit()



    feijao_verde_passo_1 = PassoModel(image_name="feijao-verde-passo-1", descricao="Coloque o feijão verde na panela de pressão e cozinhe por aproximadamente 10 minutos.",
    cronometro=600, dica = None,receita_id=receita_feijao_verde.id)
    feijao_verde_passo_1.tecnicas.append(tecnica_panela_pressao)

    db.session.add(feijao_verde_passo_1)
    db.session.commit()

    feijao_verde_passo_2 = PassoModel(image_name="feijao-verde-passo-2", descricao="Retire do fogo e espere sair toda a pressão. Em seguida escorra o feijão, despreze a água.",
    cronometro=None,dica=None, receita_id=receita_feijao_verde.id)

    db.session.add(feijao_verde_passo_2)
    db.session.commit()

    feijao_verde_passo_3 = PassoModel(image_name="feijao-verde-passo-3", descricao="Corte a cebola e o alho em pedaços bem pequenos e refogue-os no azeite de oliva com o caldo de galinha.",
    cronometro=None,dica="Deixe o alho dourar, mas cuidado para não queimá-lo.", receita_id=receita_feijao_verde.id)

    db.session.add(feijao_verde_passo_3)
    db.session.commit()

    #feijao_verde_dica_1 = DicaModel(descricao="Deixe o alho dourar, mas cuidado para não queimá-lo.", passo_id=feijao_verde_passo_3.id)

#    db.session.add(feijao_verde_dica_1)
#    db.session.commit()

    feijao_verde_passo_4 = PassoModel(image_name="feijao-verde-passo-4", descricao="Acrescente o feijão aos poucos e vá misturando. Em seguida acrescente o queijo e pra finalizar o cheiro verde.",
    cronometro=None,dica="Se você sentir necessidade pode acrescentar uma pitada de sal.\nAcrescente um pouco mais de cheiro verde após apagar o fogo para decorá-lo.", receita_id=receita_feijao_verde.id)

    db.session.add(feijao_verde_passo_4)
    db.session.commit()

#    feijao_verde_dica_2 = DicaModel(descricao="Se você sentir necessidade pode acrescentar uma pitada de sal.", passo_id=feijao_verde_passo_4.id)

#    db.session.add(feijao_verde_dica_2)
#    db.session.commit()

#    feijao_verde_dica_3 = DicaModel(descricao="Acrescente um pouco mais de cheiro verde após apagar o fogo para decorá-lo.", passo_id=feijao_verde_passo_4.id)

#    db.session.add(feijao_verde_dica_3)
#    db.session.commit()

    arroz_brocolis_passo_1  = PassoModel(image_name="arroz-brocolis-passo-1", descricao="Em uma panela junte o alho e o óleo e deixe dourar. Em seguida acrescente o arroz e refoque bem.",
    cronometro=None, dica="Nesse momento a água já deve estar no fogo para ferver.", receita_id=receita_arroz_brocolis.id)

    db.session.add(arroz_brocolis_passo_1)
    db.session.commit()

#    arroz_brocolis_dica_1 = DicaModel(descricao="Nesse momento a água já deve estar no fogo para ferver.", passo_id=arroz_brocolis_passo_1.id)

#    db.session.add(arroz_brocolis_dica_1)
#    db.session.commit()

    arroz_brocolis_passo_2 = PassoModel(image_name="arroz-brocolis-passo-2", descricao="Coloque sal a gosto e misture, acrescente a água fervente e deixe cozinhar.",
    cronometro=None, dica="Você já pode ir picando o brócolis enquanto o arroz cozinha.", receita_id=receita_arroz_brocolis.id)

    db.session.add(arroz_brocolis_passo_2)
    db.session.commit()

#    arroz_brocolis_dica_2 = DicaModel(descricao="Você já pode ir picando o brócolis enquanto o arroz cozinha.", passo_id=arroz_brocolis_passo_2.id)

#    db.session.add(arroz_brocolis_dica_2)
#    db.session.commit()

    arroz_brocolis_passo_3 = PassoModel(image_name="arroz-brocolis-passo-3", descricao="Com o arroz cozido solte todo o arroz com uma colher.",
    cronometro=None,dica=None, receita_id=receita_arroz_brocolis.id)

    db.session.add(arroz_brocolis_passo_3)
    db.session.commit()

    arroz_brocolis_passo_4 = PassoModel(image_name="arroz-brocolis-passo-4", descricao="Em outra panela acrescente o brócolis picado com o azeite e refogue o brócolis.",
    cronometro=None,dica="Você pode utilizar a manteiga no lugar do azeite.", receita_id=receita_arroz_brocolis.id)

    db.session.add(arroz_brocolis_passo_4)
    db.session.commit()

#    arroz_brocolis_dica_3 = DicaModel(descricao="Você pode utilizar a manteiga no lugar do azeite.", passo_id=arroz_brocolis_passo_4.id)

#    db.session.add(arroz_brocolis_passo_4)
#    db.session.commit()

    arroz_brocolis_passo_5 = PassoModel(image_name="arroz-brocolis-passo-5", descricao="Misture o arroz na panela do brócolis aos poucos sempre mehendo. Quando tiver bem misturado você pode apagar o fogo e servir.",
    cronometro=None, dica=None, receita_id=receita_arroz_brocolis.id)

    db.session.add(arroz_brocolis_passo_5)
    db.session.commit()


    ovo_passo_1 = PassoModel(image_name="ovo-passo-1", descricao="Numa tigela pequena quebre o ovo, com cuidado para não furar a gema.", cronometro=None,
    dica=None, receita_id = receita_ovo.id)
    ovo_passo_1.tecnicas.append(tecnica_ovo)

    db.session.add(ovo_passo_1)
    db.session.commit()

    ovo_passo_2 = PassoModel(image_name="ovo-passo-2", descricao="Leve uma frigideira antiaderente ao fogo baixo e espalhe o azeite", cronometro=None,
    dica=None, receita_id = receita_ovo.id)
    ovo_passo_2.tecnicas.append(tecnica_utensilios)
    ovo_passo_2.tecnicas.append(tecnica_panelas)

    db.session.add(ovo_passo_2)
    db.session.commit()

    ovo_passo_3 = PassoModel(image_name="ovo-passo-3", descricao="Com cuidado, transfira o ovo para a frigideira e deixe cozinhar por cerca de 1 minuto. Com uma espátula, vá puxando a borda da clara para perto da gema, para manter o formato arredondado do ovo.",
    cronometro=60, dica=None, receita_id = receita_ovo.id )

    db.session.add(ovo_passo_3)
    db.session.commit()

    ovo_passo_4 = PassoModel(image_name="ovo-passo-4", descricao="Assim que a clara começar a firmar, tempere com o sal e a pimenta, tampe a frigideira e deixe por mais 1 minuto para o ovo terminar de fritar mas a gema ainda ficar mole. O vapor permite que a clara cozinhe por igual sem a base do ovo queimar. Sirva a seguir.",
    cronometro=60, dica=None, receita_id= receita_ovo.id)

    db.session.add(ovo_passo_4)
    db.session.commit()


    macarrao_passo_1 = PassoModel(image_name="macarrao-passo-1", descricao="Em uma panela, adicione a água e espere ferver.", cronometro=None,
    dica="Você pode cortar em pedaços medianos a calabresa e a cebola enquanto espera.", receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_1)
    db.session.commit()

    macarrao_passo_2 = PassoModel(image_name="macarrao-passo-2", descricao="Adicione o sal e 1 colher de azeite, mexa em seguida, adicione o macarrão",
    cronometro=None, dica="Para saber a quantidade certa de macarrão, dê uma olhada na técnica de medidas", receita_id=receita_macarrao.id)
    macarrao_passo_2.tecnicas.append(tecnica_medidas)

    db.session.add(macarrao_passo_2)
    db.session.commit()

    macarrao_passo_3 = PassoModel(image_name="macarrao-passo-3", descricao="Deixe cozinhar por 7 min e mexa algumas vezes. Após o tempo, caso ache muito duro deixe mais 1 minuto e confira de novo.",
    cronometro=420, dica=None, receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_3)
    db.session.commit()

    macarrao_passo_4 = PassoModel(image_name="macarrao-passo-4", descricao="Reserve o macarrão em um escorredor e leve ao fogo o azeite e a cebola em fogo baixo até dourar.",
    cronometro=None, dica=None, receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_4)
    db.session.commit()

    macarrao_passo_5 = PassoModel(image_name="macarrao-passo-5", descricao="Ainda em fogo baixo, acrescente a calabresa e deixe fritando por 5min, mexendo sempre para não queimar. Caso queira mais crocante, pode deixar mais um pouco.",
    cronometro=300, dica=None, receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_5)
    db.session.commit()

    macarrao_passo_6 = PassoModel(image_name="macarrao-passo-6", descricao="Adicione o molho de tomate e a pimenta do reino, mexendo até ferver.",
    cronometro=None, dica=None, receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_6)
    db.session.commit()

    macarrao_passo_7 = PassoModel(image_name="macarrao-passo-7", descricao="Por ultimo, adicione o macarrão e o queijo, mexa e sirva a seguir.",
    cronometro=None, dica=None, receita_id = receita_macarrao.id)

    db.session.add(macarrao_passo_7)
    db.session.commit()


    cerveja_passo_1 = PassoModel(image_name="cerveja-passo-1", descricao="Em uma panela coloque o açúcar mascavo e duas colheres de água.",
    cronometro=None, dica=None, receita_id=receita_cerveja.id)
    cerveja_passo_1.tecnicas.append(tecnica_panelas)
    cerveja_passo_1.tecnicas.append(tecnica_acucar)

    db.session.add(cerveja_passo_1)
    db.session.commit()

    cerveja_passo_2 = PassoModel(image_name="cerveja-passo-2", descricao="Leve ao fogo baixo por aproximadamente 5 minutos.", cronometro=300,
    dica="Comece a contar os 5 minutos após começar a ferver e formar bolhas", receita_id=receita_cerveja.id)

    db.session.add(cerveja_passo_2)
    db.session.commit()

    cerveja_passo_3 = PassoModel(image_name="cerveja-passo-3", descricao="Após desligar o fogo, adicione a manteiga e mexa até derreter.",
    cronometro=None, dica=None, receita_id=receita_cerveja.id)

    db.session.add(cerveja_passo_3)
    db.session.commit()

    cerveja_passo_4 = PassoModel(image_name="cerveja-passo-4", descricao="Adicione o suco de limão, o sal e a essência de baunilha.",
    cronometro=None, dica=None, receita_id=receita_cerveja.id)

    db.session.add(cerveja_passo_4)
    db.session.commit()

    cerveja_passo_5 = PassoModel(image_name="cerveja-passo-5", descricao="Adicione a nata ou o creme de leite fresco e misture bem.",
    cronometro=None, dica=None,receita_id=receita_cerveja.id )

    db.session.add(cerveja_passo_5)
    db.session.commit()

    cerveja_passo_6 = PassoModel(image_name="cerveja-passo-6", descricao="A proporção ideal é de 2 colheres de sopa para 150ml de água com gás.",
    cronometro=None, dica="Utilize a água com gás gelada para um melhor preparo",receita_id=receita_cerveja.id )

    db.session.add(cerveja_passo_6)
    db.session.commit()


    bolinho_passo_1 = PassoModel(image_name="bolinho-chuva-1", descricao="Bata os ovos com e uma xícara de açúcar até dissolver o açúcar.",
    cronometro=None, dica="Você pode pegar um pouco da mistura nos dedos e sentir o açúcar. Se estiver liso é porque ficou pronto.",
    receita_id=receita_bolinho_chuva.id)


    db.session.add(bolinho_passo_1)
    db.session.commit()

    bolinho_passo_2 = PassoModel(image_name="bolinho-chuva-2", descricao="Junte o leite e a farinha de trigo peneirada.", cronometro=None,
    dica=None, receita_id=receita_bolinho_chuva.id)

    db.session.add(bolinho_passo_2)
    db.session.commit()

    bolinho_passo_3 = PassoModel(image_name="bolinho-chuva-3", descricao="Acrescente o fermento no final e misture bem, a massa tem consistência mole.",
    cronometro=None, dica=None, receita_id=receita_bolinho_chuva.id)

    db.session.add(bolinho_passo_3)
    db.session.commit()

    bolinho_passo_4 = PassoModel(image_name="bolinho-chuva-4", descricao="Aqueça o óleo e com ajuda de uma colher pingue no óleo quente colheradas de massa. O óleo deve estar quente, mas não muito, se estiver muito quente seus bolinhos vão dourar por fora e ficar crú por dentro, quando ficar muito quente abaixe um pouco o fogo e volte a fritar.",
    cronometro=None, dica="Cuidado para o óleo não espirrar. Coloque a colher próxima ao óleo para não se queimar.", receita_id=receita_bolinho_chuva.id)

    db.session.add(bolinho_passo_4)
    db.session.commit()

    bolinho_passo_5 = PassoModel(image_name="bolinho-chuva-5", descricao="Frite até que esteja dourado e transfira para o papel toalha para escorrer o excesso de óleo.",
    cronometro=None, dica=None, receita_id=receita_bolinho_chuva.id)
    bolinho_passo_5.tecnicas.append(tecnica_frituras)


    db.session.add(bolinho_passo_5)
    db.session.commit()

    bolinho_passo_6 = PassoModel(image_name="bolinho-chuva-6", descricao="Misture 3 colheres de açúcar com uma de canela e passe os bolinhos.", cronometro=None,
    dica=None, receita_id=receita_bolinho_chuva.id)

    db.session.add(bolinho_passo_6)
    db.session.commit()

    panqueca_passo_1 = PassoModel(image_name="panqueca-passo-1", descricao="Amassar bem a Banana", cronometro=None, dica=None, receita_id=receita_panqueca.id)

    db.session.add(panqueca_passo_1)
    db.session.commit()

    panqueca_passo_2 = PassoModel(image_name="panqueca-passo-2", descricao="Misturar muito bem a farinha de aveia, o fermento e o bicarbonato de sódio",
    cronometro=None, dica=None, receita_id=receita_panqueca.id)

    db.session.add(panqueca_passo_2)
    db.session.commit()

    panqueca_passo_3 = PassoModel(image_name="panqueca-passo-3", descricao="Misturar bem o restante dos ingredientes (Banana, geleia de arroz, iogurte e ovo)",
    cronometro=None, dica="Use uma vara de arames para fazer a mistura", receita_id=receita_panqueca.id)

    db.session.add(panqueca_passo_3)
    db.session.commit()

    panqueca_passo_4 = PassoModel(image_name="panqueca-passo-4", descricao="Colocar ao lume uma frigideira anti-aderente e verter, com a ajuda de uma concha, um pouco de massa",
    cronometro=None, dica=None, receita_id=receita_panqueca.id)

    db.session.add(panqueca_passo_4)
    db.session.commit()

    panqueca_passo_5 = PassoModel(image_name="panqueca-passo-5", descricao="Deixar cozinhar de um lado, até se formarem bolhas de ar na superfície e virar cuidadosamente, com a ajuda de uma espátula.",
    cronometro=None, dica="Usar uma espátula de inox, que se agarra menos à massa", receita_id=receita_panqueca.id)

    db.session.add(panqueca_passo_5)
    db.session.commit()

    panqueca_passo_6 = PassoModel(image_name="panqueca-passo-6", descricao="Retirar do calor e colocar a panqueca num prato de servir, repetindo a operação anterior até a massa se esgotar",
    cronometro=None, dica=None, receita_id = receita_panqueca.id)

    db.session.add(panqueca_passo_6)
    db.session.commit()

    panqueca_passo_7 = PassoModel(image_name="panqueca-passo-7", descricao="Servir as panquecas com os mirtilos regados com um fio de geleia, agave ou mel",
    cronometro=None, dica=None, receita_id = receita_panqueca.id)

    db.session.add(panqueca_passo_7)
    db.session.commit()

    frango_passo_1 = PassoModel(image_name="frango-recheado-passo-1", descricao="Divida um peito de frango em dois", cronometro=None,
    dica=None, receita_id=receita_frango.id)

    db.session.add(frango_passo_1)
    db.session.commit()

    frango_passo_2 = PassoModel(image_name="frango-recheado-passo-2", descricao="Corte cada metade ao meio, como um pãozinho", cronometro=None,
    dica=None, receita_id=receita_frango.id)

    db.session.add(frango_passo_2)
    db.session.commit()

    frango_passo_3 = PassoModel(image_name="frango-recheado-passo-3", descricao="Tempere com sal e pimenta e coloque o recheio que quiser: coloquei um tiquinho de requeijão, tomate e orégano",
    cronometro=None, dica="Use uma vara de arames para fazer a mistura", receita_id=receita_frango.id)

    db.session.add(frango_passo_3)
    db.session.commit()

    frango_passo_4 = PassoModel(image_name="frango-recheado-passo-4", descricao="Feiche com palitos", cronometro=None, dica=None,
    receita_id=receita_frango.id)

    db.session.add(frango_passo_4)
    db.session.commit()

    frango_passo_5 = PassoModel(image_name="frango-recheado-passo-5", descricao="Grelhe na frigideira no fogo bem alto, apenas para selar, dos dois lados",
    cronometro=None, dica=None, receita_id=receita_frango.id)

    db.session.add(frango_passo_5)
    db.session.commit()

    frango_passo_6 = PassoModel(image_name="frango-recheado-passo-6", descricao="Transfira para um refratário e cubra com molho de tomate",
    cronometro=None, dica=None, receita_id=receita_frango.id)

    db.session.add(frango_passo_6)
    db.session.commit()

    frango_passo_7 = PassoModel(image_name="frango-recheado-passo-7", descricao=" Leve ao forno preaquecido a 180 graus por 20 minutinhos - tá pronto!",
    cronometro=1200, dica=None, receita_id=receita_frango.id)

    db.session.add(frango_passo_7)
    db.session.commit()


    biscoito_passo_1 = PassoModel(image_name="biscoito-fit-banana-1", descricao="Coloque o forno para aquecer a 190 graus", cronometro=None,
    dica="Se você não encontrar quinua em flocos pode substituí-la por aveia em flocos, o resultado fica igualmente bom, mas aí a receita passará a conter glúten",
    receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_1)
    db.session.commit()

    biscoito_passo_2 = PassoModel(image_name="biscoito-fit-banana-2", descricao="Amasse bem as bananas com um garfo", cronometro=None,
    dica=None, receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_2)
    db.session.commit()

    biscoito_passo_3 = PassoModel(image_name="biscoito-fit-banana-3", descricao="Misture a quinua em flocos e a canela até obter uma massa cremosa e homogênea",
    cronometro=None, dica="Use uma vara de arames para fazer a mistura", receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_3)
    db.session.commit()

    biscoito_passo_4 = PassoModel(image_name="biscoito-fit-banana-4", descricao="Unte levemente uma assadeira com azeite (ou use um tapetinho de forno forrando uma assadeira, conhecido como Silpat, e aí não precisa untar)",
    cronometro=None, dica=None, receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_4)
    db.session.commit()

    biscoito_passo_5 = PassoModel(image_name="biscoito-fit-banana-5", descricao="Espalhe a massa em pequenas colheradas, modelando os biscoitos com a própria colher e mantendo uma distância de alguns centímetros entre um biscoito e outro",
    cronometro=None, dica="usar uma espátula de inox, que se agarra menos à massa", receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_5)
    db.session.commit()

    biscoito_passo_6 = PassoModel(image_name="biscoito-fit-banana-6", descricao="Asse por 30 minutos, ou até perceber que os biscoitos estão dourados e firmes.",
    cronometro=1800, dica=None, receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_6)
    db.session.commit()

    biscoito_passo_7 = PassoModel(image_name="biscoito-fit-banana-7", descricao="Desligue o forno e deixe que esfriem lá dentro.",
    cronometro=None, dica=None, receita_id=receita_biscoito_fit.id)

    db.session.add(biscoito_passo_7)
    db.session.commit()


    salada_passo_1 = PassoModel(image_name="salada-forno-passo-1", descricao="Fatie a berinjela, a abobrinha e os tomates", cronometro=None,
    dica=None, receita_id=receita_salada.id)

    db.session.add(salada_passo_1)
    db.session.commit()

    salada_passo_2 = PassoModel(image_name="salada-forno-passo-2", descricao="Disponha no refratário sobrepondo umas sobre as outras, criando o efeito dominó",
    cronometro=None, dica=None, receita_id=receita_salada.id)

    db.session.add(salada_passo_2)
    db.session.commit()

    salada_passo_3 = PassoModel(image_name="salada-forno-passo-3", descricao="Cubra com azeitonas", cronometro=None,
    dica="Use uma vara de arames para fazer a mistura", receita_id=receita_salada.id)

    db.session.add(salada_passo_3)
    db.session.commit()

    salada_passo_4 = PassoModel(image_name="salada-forno-passo-4", descricao="Tempere com sal, pimenta, ervas frescas ou secas",
    cronometro=None, dica=None, receita_id=receita_salada.id)

    db.session.add(salada_passo_4)
    db.session.commit()

    salada_passo_5 = PassoModel(image_name="salada-forno-passo-5", descricao="Finalize com um fio de azeite e leve ao forno preaquecido a 180º por aproximadamente 30 minutos ou até que o garfo entre com facilidade.",
    cronometro=1800, dica="usar uma espátula de inox, que se agarra menos à massa", receita_id=receita_salada.id)

    db.session.add(salada_passo_5)
    db.session.commit()
