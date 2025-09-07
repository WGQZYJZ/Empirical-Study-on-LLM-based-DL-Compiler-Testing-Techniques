
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer  = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        vq  = torch.randn(35760, 10).div(1e-4 + 3.8913499354511387).mul(-1.).tanh()
        vk  = vq  # Assign the query value to key and value values. These values will be used in the model forward method. The shape of these values is (35760, 2)
        vv  = torch.nn.functional.one_hot(torch.tensor([1] * 35760), num_classes=2).to(dtype=vq.dtype).float()
        vqk  = torch.matmul(vq, vk.transpose(-2, -1)) # Compute the dot product of the query and key values. 
        scaled_vqk  = vqk .div(torch.tensor([3.8913499354511387]).to(vq.device).expand(scaled_qk.size(-2))) # Scale the dot product by an inverse scale factor
        softmax_qk  = scaled_vqk .softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output 
        return dropout_qk .matmul(vv)
 
# Initializing the model
m  = Model()


# Inputs to the model