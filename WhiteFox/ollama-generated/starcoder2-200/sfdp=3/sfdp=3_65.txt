
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        v0 = torch.matmul(query1, key2) # Compute the dot product of the query and key tensors
        v1  = v0 * scale_factor # Scale the dot product by a factor
        v3  = torch.nn.functional.softmax(v1, dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)  
        v5  = v2.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v6


# Initializing the model
m  = Model()

# Inputs to the model (replace with your inputs here!)
query1  = torch.randn(3,4096)  
key2    = torch.randn(5,4096)  

# Setting hyperparameters for model (you can change these values or add new ones as needed)
scale_factor = 0.78125
dropout_p    = 0.3

 # Call the forward function of the model to get the output of the model, assuming that the model was loaded correctly and the inputs were already set up properly. Note that you will need to use torch.no_grad() when making inference to avoid activating autograd which would allow gradients to backpropagate through this step
output  = m(query1, key2)

