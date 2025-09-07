
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      conv  = torch.nn.Conv2d(3, 5, 4)
      bn   = torch.nn.BatchNorm2d(5)
      output = torch.nn.functional.batch_norm(conv(x1))


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor  = torch.randn(3, 4, 50, 86) # input with the shape of [N, C, H, W]
x1 = torch.randn(2, 4, 50, 86)

__output__   = m(input_tensor), 