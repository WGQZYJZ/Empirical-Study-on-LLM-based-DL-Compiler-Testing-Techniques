

model  = torch.nn.Conv2d(3, 8, 1)
__output__  = model(torch.randn(1, 3, 64, 64))

# Initializing the model
m = model


x1 = torch.randn(1, 3, 64, 64)
