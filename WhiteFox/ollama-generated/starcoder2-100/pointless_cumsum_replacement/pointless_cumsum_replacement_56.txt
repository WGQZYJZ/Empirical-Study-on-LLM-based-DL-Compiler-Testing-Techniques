
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0: torch.Tensor) -> torch.Tensor:
            t1  =  x0.clone()
            t2  =  t1 * 3
            return t2

# Initializing the model
m = Model()

 # Inputs to the model
__input_data__ = torch.tensor(1.)

 ## The generated source code contains invalid syntax. You need to add more pytorch APIs or modify existing ones. 
You can also try to re-generate this model if you know which pytorch APIs are allowed. 

