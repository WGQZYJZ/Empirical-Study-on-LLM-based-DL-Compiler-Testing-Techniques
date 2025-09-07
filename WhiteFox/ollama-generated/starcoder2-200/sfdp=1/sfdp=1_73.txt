

## Initializing the model
m  = Model()

## Inputs to the model
x1 = torch.randn(32, 50, 768)
x2 = torch.randn(32, 192)
x3 = torch.randn(32)

__outputs__  = m(x1, x2, x3)

