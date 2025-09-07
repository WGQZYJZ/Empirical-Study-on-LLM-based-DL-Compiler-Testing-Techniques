
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.Tensor([4])
        self.key  = torch.randn(3, 8) # Replace with the value of the key tensor
        self.value = torch.randn(128, 8, 56, 56) # Replace with the value of the value tensor
 
    def forward(self):
        qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor # Compute dot product using query and key tensors
        scaled_qk = qk / inv_scale_factor # Scale dot product by inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.7)
        output = dropout_qk.matmul(value)

# Initializing the model
m = Model()

