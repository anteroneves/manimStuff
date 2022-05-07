from manim import *

class EixosArgand(Scene):
    def construct(self): 
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{fouriernc}")
        eixos = Axes(
            x_range=[-2,2,1],
            y_range=[-2,2,1],
            tips=True,
            axis_config={"include_ticks":False},
            )
        self.play(FadeIn(eixos))
        #self.add(eixos)
        LabelRe = Tex(r"\(\Re(z)\)").move_to(RIGHT*6+.5*DOWN)
        LabelIm = Tex(r"\(\Im(z)\)").move_to(LEFT*1 + 3*UP)
        self.play(Write(LabelRe),Write(LabelIm))
        #self.add(LabelRe,LabelIm)
        PtZ = Cross(scale_factor=.05,stroke_width=3).move_to(RIGHT*3+UP*1.5) # Desenha uma cruz na posição (3,1.5) 
        LabelZ = Tex(r"\footnotesize\(z\)").next_to(PtZ,UP,buff=.1) # Desenha o label do ponto z por cima do PtZ usando LaTeX
        #self.add(PtZ) 
        #self.add(LabelZ)
        self.play(Create(PtZ),Write(LabelZ))
        PtA = Dot(radius=.08,color=BLUE,fill_opacity=.5)
        RePtA = Tex(r"\footnotesize\(a\)").next_to(PtA,DOWN,buff=.1)
        RePtA.add_updater( # a letra "a" acompanha o ponto ao longo do eixo real.
            lambda mob: mob.next_to(PtA,DOWN,buff=.1)
        )
        self.play(Create(PtA))
        self.play(Write(RePtA))
        self.play(PtA.animate.shift(RIGHT*3), run_time=3)
        RePtA.suspend_updating() # Suspende a movimentação do "a" por baixo do ponto azul feita no updater.
        
        ImPtA = Tex(r"\footnotesize\(b\)").next_to(PtA,LEFT, buff=3)
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
        self.wait(2)


