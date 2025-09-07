
class Model(torch.nn.Module):
    def __init__(self, k1, k2):
        super().__init__()
        self.mm  = torch.nn.Linear(k1, k2)

    def forward(self, x1):
        v1  = self.mm(x1) 
        return v1

# Initializing the model
m  = Model(507836940, 39290430)

 # Inputs to the model
input1  = torch.randn(k1, dtype=torch.float32) + input_tensor
input2  = torch.randn(dtype=torch.float32)  + 1
input3  = torch.randn(k1, k2, dtype=torch.float32) + input_tensor
input4  = torch.randn(dtype=torch.float32)   * -0.5

 # Initializing the model
 m  = Model(int(input1[0].size()[0]), int(input2[0].size()[0]))

  # Inputs to the model
  input1  = torch.randn(k1, dtype=torch.float32) + input_tensor
  input2  = torch.randn(dtype=torch.float32) * -0.5
__output__  = m(input1, input2)

