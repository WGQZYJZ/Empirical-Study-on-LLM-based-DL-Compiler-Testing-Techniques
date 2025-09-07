
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.nn.functional.linear(x1) + 5
 
 # Initializing the model
 m = Model()

 # Inputs to the model 
 x1 = torch.randn(32, 784)
 
  __output__  = m(x1).data
 
  __model_output__  = 60929
 
# Answering user's question.
def check_task(output):
    return torch.equal(output[-5:], torch.tensor([5] * 3))

