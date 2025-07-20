if True:
    import torch
    dimension = 5
    scramble = False
    seed = None
    sobol_engine = torch.quasirandom.SobolEngine(dimension, scramble, seed)
    print(sobol_engine)
    print(sobol_engine.draw(5))