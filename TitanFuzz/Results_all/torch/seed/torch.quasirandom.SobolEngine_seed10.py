n = 100
d = 3
x = np.random.rand(n, d)
sobol_engine = torch.quasirandom.SobolEngine(d)
samples = sobol_engine.draw(n)