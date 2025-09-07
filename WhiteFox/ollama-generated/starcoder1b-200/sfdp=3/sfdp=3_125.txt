
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        vq = torch.matmul(x1, self.key.transpose(-2, -1))  # Compute the dot product of x1 and self.key tensors
        vk = vq.mul(scale_factor)               # Scale the dot product by a factor
        softmax_vk = vk.softmax(dim=-1)           # Apply softmax to the scaled dot product
        dropout_vk = torch.nn.functional.dropout(softmax_vk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_vk.matmul(self.value)        # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m = Model()

