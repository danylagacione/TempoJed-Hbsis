# As cartas utilizadas e valores serão conforme abaixo:
# "2" => 2
# "3" => 3
# "4" => 4
# "5" => 5
# "6" => 6
# "7" => 7
# "8" => 8
# "9" => 9
# "10" => 10
# "A" => 1
# "J" => 10
# "Q" => 10
# "K" => 10
#
# O jogo deverá embaralhar as cartas acima. O jogo deve pedir para o jogador virar uma cartão,
# quando ele virar, deverá apresentar o score de acordo com a carta.
#
# Obs.: O "A" terá o valor 1 quando tiver outro número já virado.
#
# Segue exemplo abaixo:
# ["A"] ==> 11
# ["A", "J"] ==> 21
# ["A", "10", "A"] ==> 12
# ["5", "3", "7"] ==> 15
# ["5", "4", "3", "2", "A", "K"] ==> 25
# jogador
#croupier
#valete, dama e reis = 10 pontos
# ás 1 ou 10 pontos de acordo com a vontade do jogador

# Jogador começa com um carta(dada pelo computador, modo randômico);
# Validar valor da carta e somar na pontuação; Perguntar para o jogador
# se ele quer continuar jogando ou parar; Se ele escolher parar, mostrar a pontuação geral;
# Se ele escolher continuar, enviar mais uma carta;
# Validar sempre a regra das cartas conforme exercício;
# A carta ÁS, na primeira vez que é tirada, vale 11.
# Se a segunda carta for uma LETRA, o ÁS continua valendo 11. Porém, se a segunda carta for um NÚMERO, o ÁS passa a valer 1.
# O objetivo do jogo é chegar aos 21  pontos, por isso é importante perguntar se o jogador quer tirar mais uma carta ou não.
# Exemplo: tenho um total de 19 pontos. O jogo vai perguntar se quero tirar mais uma carta ou não. Se eu escolher tirar, e sair um 2, eu venço o jogo.
# Se sair 3, eu perco. Se sair 1, posso jogar novamente ou parar... E assim por diante...




