
class Model(torch.nn.Module):
    def __init__(self, N=32):
        super().__init__()
        self.fc  = torch.nn.Linear(N * N + 4096, 1)
 
    def forward(self, input1, input2):
       t1 = torch.mm(input1, input2)
       t2 = torch.cat([t1] * 32768, dim=len(list(self._modules.values())[0].parameters()))

       return self.fc(t2)
# Initializing the model
N  = 32
m  = Model(N)

 # Inputs to the model (The second input is a dummy variable; it can be replaced by the first input when the user runs the program)
x1, x2 = torch.randn((N + 64, N)), torch.rand((N * N + 3))
__output__  = m(x1, x2)

