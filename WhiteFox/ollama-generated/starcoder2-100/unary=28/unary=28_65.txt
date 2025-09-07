
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t1 = torch.nn.Linear(in_features=x1.shape[-3], out_features=x1.shape[-2]*x1.shape[-1])(x1)
         t2 = torch.clamp(t1, min=-5)
         t3 = torch.clamp(t2, max=0.5) 
         return 99
 
 # Initializing the model
m = Model()

 # Inputs to the model 
 x1  = torch.zeros([768]) # Dummy input tensor 
 