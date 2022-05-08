from manim import *

class EixosArgand(Scene):
    def construct(self): 
        eixos = Axes(
            x_range=[-2,2,1],
            y_range=[-2,2,1],
            tips=True,
            axis_config={"include_ticks":False},
            )
        self.play(FadeIn(eixos))
        LabelRe = Tex(r"\(\Re(z)\)").move_to(RIGHT*6+.5*DOWN)
        LabelIm = Tex(r"\(\Im(z)\)").move_to(LEFT*1 + 3*UP)
        self.play(Write(LabelRe),Write(LabelIm))
        PtZ = Cross(scale_factor=.05,stroke_width=3).move_to(RIGHT*3+UP*1.5) # Desenha uma cruz na posição (3,1.5) 
        LabelZ = Tex(r"\footnotesize\(z\)").next_to(PtZ,UP,buff=.1) # Desenha o label do ponto z por cima do PtZ usando LaTeX
        self.play(Create(PtZ),Write(LabelZ)) # animação: cria o ponto z e escreve o seu label
        PtA = Dot(radius=.08,color=BLUE,fill_opacity=.5) # Define um ponto que surge na origem.
        RePtA = Tex(r"\footnotesize\(a\)").next_to(PtA,DOWN,buff=.1) # define o texto
        RePtA.add_updater( # a letra "a" acompanha o ponto ao longo do eixo real.
            lambda mob: mob.next_to(PtA,DOWN,buff=.1)
        )
        self.play(Create(PtA)) # animação: cria o ponto azul
        self.play(Write(RePtA)) # animação: cria o label da parte real do ponto azul
        self.play(PtA.animate.shift(RIGHT*3), run_time=3) # animação: move o ponto azul para a parte real do número z

        RePtA.suspend_updating() # Suspende a movimentação do "a" por baixo do ponto azul feita no updater.
        
        ImPtA = Tex(r"\footnotesize\(b\)").next_to(PtA,LEFT, buff=3) # Define o texto para a parte imaginária do número z.
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
        self.play(PtA.animate.shift(UP*1.5),run_time=3)

        PtAux1 = Dot([6,0,0],fill_opacity=0)
        SemiReta = DashedLine([0,0,0],PtAux1)
        SemiReta.add_updater(
            lambda mob: mob.become(DashedLine([0,0,0],PtAux1))
        )
        l1 = Line(ORIGIN,RIGHT) # Linha 1 para fazer o ângulo theta
        l2 = Line(ORIGIN,RIGHT) # Linha 2 para fazer o ângulo theta, esta é a linha a movimentar
        l2.rotate(0.46364,about_point=ORIGIN) # Definição da rotação a aplicar à linha 2

        theta = Angle(l1,l2,radius=.5).set_color(RED) # Definição do ângulo theta que vai ser alterado de acordo com a rotação da linha 2.
        theta.add_updater( # Updater para fazer theta acompanhar a rotação da linha 2
            lambda mob:mob.become(Angle(l1,l2,radius=.5).set_color(RED))
        )
        theta_label = Tex(r"\tiny\(\theta\)").next_to(theta,RIGHT,buff=.1).set_color(RED) # Definição do label do ângulo theta
        theta_label.add_updater( # Definição do updated para fazer o label acompanhar o crescimento do ângulo theta
            lambda mob: mob.next_to(theta,RIGHT,buff=.1).set_color(RED)
        )
        self.play(Create(SemiReta),run_time=.5)
        self.add(theta_label)
        self.play(Create(theta),Rotate(PtAux1,angle=0.463647609,about_point=ORIGIN))

        PtTrig = Dot(radius=.08,color=RED,fill_opacity=.5)
        self.play(Create(PtTrig))
        moduloz = Line(ORIGIN,PtTrig.get_center())
        moduloz.add_updater(
            lambda mob: mob.become(Line(ORIGIN,PtTrig.get_center()))
        )
        self.add(moduloz)
        chaveta = BraceBetweenPoints(PtTrig.get_center(),[0,0,0]).set_color(RED)
        chaveta.add_updater(
            lambda mob: mob.become(BraceBetweenPoints(PtTrig.get_center(),[0,0,0]).set_color(RED))
        )
        chaveta_label = Tex(r"\tiny\(\abs{z}\)").next_to(moduloz.get_midpoint(),UP*2+LEFT,buff=.2).set_color(RED)
        chaveta_label.add_updater(
            lambda mob: mob.next_to(moduloz.get_midpoint(),UP*2+LEFT,buff=.2).set_color(RED)
        )
        self.play(Create(chaveta),Write(chaveta_label))
        self.play(Transform(PtTrig,PtZ))
        self.wait(2)
