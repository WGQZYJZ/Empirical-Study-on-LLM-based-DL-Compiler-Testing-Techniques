
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(8, 20) # Define the query transformation
        self.key   = torch.nn.Linear(32, 40) # Define the key transformation
        self.value = torch.nn.Linear(64, 125) # Define the value transformation

    def forward(self, qkv):
        scale_factor = torch.sqrt(torch.tensor([8])).cuda()
        inv_scale_factor = torch.rsqrt(torch.tensor([8])).cuda()
 
        vq = self.query(qkv[:, 0]) # Apply the query transformation to the first dimension of the input
        vk = self.key(qkv[:, 1:]) * scale_factor # Apply the key transformation to the remaining dimensions and then divide by a scaling factor
        
        qk = torch.matmul(vq, vk.transpose(-2, -1)) # Compute the dot product between the query output and the key output
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value(qkv[:, 0]))  # Compute the dot product between the dropout output and the value transformation
        
        return output


# Initializing the model
m  = Model().cuda()
