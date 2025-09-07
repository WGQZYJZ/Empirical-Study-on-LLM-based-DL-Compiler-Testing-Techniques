
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1):
         return [
             torch.nn.functional.linear(x1[i], self.linear.weight), 
             torch.nn.functional.dropout(torch.rand_like(x1[i]), p=0.3)]


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = [
    torch.randn(5, 2), 
    torch.randn(4, 2), 
    torch.randn(3, 2) ] 
 __output__= m(x1)

[
  [Tensor of size: (5, 10)], 
  [Tensor of size: (4, 10), 0.3, False],  
  [Tensor of size: (3, 10), 0.3, False]  
]

# Description of requirements for the fallback_random configuration on CPU devices.
This model contains two dropout nodes, and two random number generation nodes. On CPU devices, these three functions will not be replaced by the `lowmem_dropout` and `rand_like` replacements, thus triggering the warning message.

