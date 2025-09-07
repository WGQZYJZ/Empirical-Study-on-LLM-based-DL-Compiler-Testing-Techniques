
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 512)
        self.key = torch.nn.Linear(1024, 512)
 
    def forward(self, input_tensor):
        vq  = self.query(input_tensor).view(-1, 16, 32) # Reduce the tensor size by a factor of 16 by performing view operation on the query and key tensors
        vk  = self.key(input_tensor).transpose(-2,-1)# Reduce the size of the second dimension in the input tensor by a factor of 32
        vqk  = torch.matmul(vq,vk) # Compute the dot product between the reduced query and key tensors
        vqks  = vqk * scale_factor# Scale the dot product by `scale_factor`
        scaled_softmax_output  = vqks.softmax(dim=-1)# Apply softmax to the scaled dot product
        dropout_scaled_softmax_output  = torch.nn.functional.dropout(scaled_softmax_output, p=0.5) # Dropout
        output  = torch.matmul(dropout_scaled_softmax_output, vk)# Compute the dot product of the dropout and value tensors
        return output

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(4, 2048)
 
__output__  = m(x1)

