
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) 
        return v1
# Initializing the model
m = Model()
 


# Inputs to the model (Replace `None` with appropriate values.)
__input_1__  = None # Input tensor for query
__input_2__  = None # Input tensor for key
__input_3__  = None # Input tensor for value

# Actual outputs of the model on given inputs. The input and output shapes may vary depending upon the provided values to the inputs.
__output__  = m(__input_1__, __input_2__, __input_3__)
