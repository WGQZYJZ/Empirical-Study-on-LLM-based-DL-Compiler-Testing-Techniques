
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, qk):
        v1 = self.conv(x1)
        scaled_qk = qk / (scale_factor ** -0.5) # Compute the scaled dot product by dividing both tensors by a constant
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v6 = dropout_qk.matmul(v1)
        return v6
 
# Initializing the model
m = Model()
q  = torch.randn(2048, 128, 32, 32)
k = torch.randn(2048, 512, 8, 8)
 

