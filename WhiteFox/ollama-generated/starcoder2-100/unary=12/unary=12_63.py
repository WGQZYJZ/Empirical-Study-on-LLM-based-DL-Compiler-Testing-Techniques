
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = nn.functional.sigmoid(v1)
        return v2 * v1

# Initializing the model and loading it to GPU memory:
m = Model()
m = m.cuda()

 # Inputs to the model
x_cpu = torch.randn(3, 8, 4096, 4096)
x_gpu = x_cpu.cuda()
 
 # Comparing results from CPU and GPU executions: 
 with torch.no_grad():
     r1 = m(x_cpu)
     r2 = m(x_gpu)

