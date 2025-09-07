
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t0  = torch.nn.functional.dropout(x1, p=0.5) 
        # Applies dropout to the input_tensor
        t1 = rand_like(t0) 

        t2  = torch.nn.functional.linear(t0, self.linear.weight, self.linear.bias)
        return t3

# Initializing the model
m  = Model()

 # Inputs to the model: 
x1  = torch.randn(4, 2) 

__output__  = m(x1)