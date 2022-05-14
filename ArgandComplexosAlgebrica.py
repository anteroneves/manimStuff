from manim import *

class EixosArgand(Scene):
    def construct(self): 

#############################
#### DEFINIÇÃO DOS EIXOS ####
#############################

        eixos = Axes( # Definição dos eixos
            x_range=[-2,2,1], # Estes três números definem x_min, x_max e step
            y_range=[-2,2,1],
            tips=True, # Definimos o valor boleano de tips para True se quisermos uma seta nos eixos.
            axis_config={"include_ticks":False,"tip_length":0.10}, # include_ticks definido como False faz com que não surjam marcações nos eixos enquanto que tip_length altera a forma da seta.
            )
        self.play(FadeIn(eixos)) # Forma como surgem os eixos na animação


#######################################################
#### DEFINIÇÃO DOS TEXTOS A COLOCAR NO REFERENCIAL ####
#######################################################


        LabelRe = Tex(r"\footnotesize\(\Re(z)\)").move_to(RIGHT*6+.3*DOWN) # Definição e posicionamento do nome do eixo real.
        LabelIm = Tex(r"\footnotesize\(\Im(z)\)").move_to(LEFT*.8 + 3*UP) # Definição e posicionamento do nome do eixo imaginário.
        LabelOrigin = Tex(r"\footnotesize\(O\)").move_to(LEFT*.3+.3*DOWN) # Definição e posicionamento do nome da origem.
        self.play(Write(LabelRe),Write(LabelIm),Write(LabelOrigin)) # Forma como aparecem os diferentes nomes.

#####################################
#### REPRESENTACAO DO AFIXO DE z ####
#####################################

        PtZ = Cross(scale_factor=.05,stroke_width=3).move_to(RIGHT*3+UP*1.5) # Desenha uma cruz na posição (3,1.5) 
        LabelZ = Tex(r"\footnotesize\(z\)").next_to(PtZ,UP,buff=.1) # Desenha o label do ponto z por cima do PtZ usando LaTeX
        self.play(Create(PtZ),Write(LabelZ)) # animação: cria o ponto z e escreve o seu label

###################
#### ALGÉBRICA ####
###################

        PtA = Dot(radius=.08,color=BLUE,fill_opacity=1) # Define um ponto que surge na origem.
        RePtA = Tex(r"\footnotesize\(a\)").next_to(PtA,DOWN,buff=.1).set_color(ORANGE) # define o texto
        RePtA.add_updater( # a letra "a" acompanha o ponto ao longo do eixo real.
            lambda mob: mob.next_to(PtA,DOWN,buff=.1)
        )
        self.play(Create(PtA)) # animação: cria o ponto azul
        self.play(Write(RePtA)) # animação: cria o label da parte real do ponto azul
        self.play(PtA.animate.shift(RIGHT*3), run_time=1) # animação: move o ponto azul para a parte real do número z

        RePtA.suspend_updating() # Suspende a movimentação do "a" por baixo do ponto azul feita no updater.
        
        ImPtA = Tex(r"\footnotesize\(b\)").next_to(PtA,LEFT, buff=3).set_color(GREEN) # Define o texto para a parte imaginária do número z.
        ImPtA.add_updater( # Mesmo que o updater aplicado RePtA
            lambda mob: mob.next_to(PtA,LEFT, buff=3)
        )
        PtACoordRe = DashedLine(PtA,[3,0,0])
        PtACoordRe.add_updater( # Transforma a linha desenhada no frame de modo a acompanhar a movimentação do PtA
            lambda mob: mob.become(DashedLine(PtA,[3,0,0]))
        )
        PtACoordIm = DashedLine(PtA,ImPtA)
        PtACoordIm.add_updater( #Mesmo que o updater aplicado a PtACoordRe
            lambda mob: mob.become(DashedLine(PtA,ImPtA))
        )
        self.play(Write(ImPtA))
        self.add(PtACoordRe,PtACoordIm)
        self.play(PtA.animate.shift(UP*1.5),run_time=1)

        FormaAlgebrica = Tex(r"\(z = a + bi\)").move_to([-3,2,0]).scale(.8)# Define, na posição indicada, o texto com uma escala alterada
    
        self.play(Write(FormaAlgebrica)) # Escreve o texto

########################
#### TRIGONOMÉTRICA ####
########################


        PtAux1 = Dot([6,0,0],fill_opacity=0) # Ponto auxiliar necessário para fazer a semi-recta a tracejado.

        #Definição do ângulo a partir de dois pontos
        d1 = Dot(point=[1.1,0,0],fill_opacity=0)
        d2 = Dot(point=[1,0,0],fill_opacity=0)

        # Desenho do ângulo theta a partir de uma CurvedArrow.
        theta = CurvedArrow(start_point=d1.get_center(),end_point=d2.get_center(),stroke_width=2,tip_length=0.10).set_color(YELLOW)
        theta.add_updater(
            lambda mob: mob.become(CurvedArrow(start_point=d1.get_center(),end_point=d2.get_center(),stroke_width=2,tip_length=0.10).set_color(YELLOW))
        )

        # Desenho da semi-recta
        Semi_Recta = DashedLine([0,0,0],PtAux1,dash_length=.1,dashed_ratio=.8).set_opacity(.5)
        Semi_Recta.add_updater(
            lambda mob: mob.become(DashedLine([0,0,0],PtAux1,dash_length=.1,dashed_ratio=.8).set_opacity(.5))
        )

        # Definição do label do ângulo a partir do nome theta mobject.
        theta_label = Tex(r"\tiny\(\theta\)").next_to(theta.get_midpoint(),RIGHT,buff=.1).set_color(YELLOW) # Definição do label do ângulo theta
        theta_label.add_updater( # Definição do updated para fazer o label acompanhar o crescimento do ângulo theta
            lambda mob: mob.next_to(theta.get_midpoint(),RIGHT,buff=.1).set_color(YELLOW)
        )

        self.play(Create(Semi_Recta),run_time=1) # Forma como surge a semi-recta e tempo completo da animação
        self.add(theta_label,theta) # Forma como aparece a primeira definição da theta e o seu label

        self.play(Rotate(PtAux1,angle=0.463647609,about_point=ORIGIN),Rotate(d2,angle=0.463647609,about_point=ORIGIN)) # Faz a animação da rotação do ponto PtAux1 (semi-recta) e do d2 (theta)

        PtTrig = Dot(radius=.08,color=RED,fill_opacity=1) # Define um ponto que aparece na origem
        PtTrig_copy = Dot(point=[3,1.5,0],radius=.08,color=RED,fill_opacity=1) # Define um ponto que é cópia do primeiro mas está na posição (3,1.5)
        self.play(Create(PtTrig)) # Cria o ponto PtTrig
        moduloz = Line(ORIGIN,PtTrig.get_center(),color=RED) # Define o segmento que une a origem ao PtTrig
        moduloz.add_updater( # Faz a actualização do segmento à medida que o PtTrig se movimenta.
            lambda mob: mob.become(Line(ORIGIN,PtTrig.get_center(),color=RED))
        )
        self.add(moduloz) # Coloca, sem animação o segmento modulo z que, para começar é apenas um ponto uma vez que o PtTrig coincide com a origem
        chaveta = BraceBetweenPoints(PtTrig.get_center(),[0,0,0]).set_color(RED) # Cria a chaveta entre o PtTrig (centro) e a origem, a ordem como se colocam estes pontos pode ser importante.
        chaveta.add_updater( # Actualiza o desenho da chaveta quando o PtTrig muda de posição.
            lambda mob: mob.become(BraceBetweenPoints(PtTrig.get_center(),[0,0,0]).set_color(RED))
        )

        chaveta_label = Tex(r"\scriptsize\(\abs{z}\)").next_to(moduloz.get_midpoint(),UP*2+LEFT,buff=.2).set_color(RED) # Adiciona o texto do módulo de z relativamente ao ponto médio do segmento.
        chaveta_label.add_updater( # Actualiza o posicionamento do texto à medida que o comprimento do moduloz muda.
            lambda mob: mob.next_to(moduloz.get_midpoint(),UP*2+LEFT,buff=.2).set_color(RED)
        )
        self.play(Create(chaveta),Write(chaveta_label)) # Cria a chaveta e o texto 
        self.play(Transform(PtTrig,PtTrig_copy)) # Faz a translação do ponto PtTrig que está na origem para o PtTrig_copy

        FormaTrigonometrica = Tex(r"\(z = \abs{z}\,e^{i\theta}\)").move_to([-3,1,0]).scale(.8) # Define, na posição indicada, o texto com uma escala alterada
    
        self.play(Write(FormaTrigonometrica)) # Escreve o texto.

        self.wait(3)
