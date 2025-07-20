x = torch.randn(10000, 2)
engine = torch.quasirandom.SobolEngine(2)
quasi_random_numbers = engine.draw(10000)