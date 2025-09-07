
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        v1  = torch.matmul(query1, key2) # Compute the dot product of two tensors 
        v2  = v1 / math.sqrt(key2[0].numel())# Scale the dot product by sqrt(number_of_elements in the first dim of the key tensor)
        v3  = torch.softmax(v2, dim=-1)# Apply softmax to the scaled dot product
        return v3
 
 # Initializing the model
 m  = Model()

 # Inputs for the model 
 query1 = torch.randn([4096], requires_grad=True)
 key2  = [torch.ones(5, 6)] 
 
 # Passing input tensors to the model and getting output tensors back.
