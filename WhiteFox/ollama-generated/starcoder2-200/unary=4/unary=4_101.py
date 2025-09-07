
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        return v6

# Initializing the model
m_initial = Model()

 # Inputs to the model
x1_intitial = torch.randn(1, 3)
__output_initial__  = m(x1_initial)

# Model definition
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 512)

    def forward(self, x1): 
        v1  = self.linear(x1)
        v2  = v1 * -1
        v3  = v1 * -75879
        v4  = torch.erf(v3) + 1

        # Multiplication in backward pass:
        def func_for_mul(v): 
            v0_grad = grad(grad(v, v1))
            return v2*v0_grad
        v6_grad = func_for_mul(v4)
        v5_grad = torch.autograd.grad(torch.sum(v3*v4), x1)[0]

        return v6*x1 + v5_grad, -75879

# Inputs to the model 
x1 = torch.randn(1, 2048) * 3 # 3 is added so that not all of the weights have the same sign. 

