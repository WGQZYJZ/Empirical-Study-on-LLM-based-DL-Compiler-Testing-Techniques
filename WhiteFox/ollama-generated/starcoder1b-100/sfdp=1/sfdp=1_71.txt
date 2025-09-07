
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2.transpose(-2, -1))
        v2 = torch.div(v2, self.inv_scale_factor)  # Scale the dot product by the inverse scale factor
        v2 = torch.softmax(v2, dim=-1)  # Apply softmax to the scaled dot product
        v2 = torch.nn.functional.dropout(v2, p=dropout_p)  # Apply dropout to the softmax output
        return torch.matmul(v2, value)


# Initializing the model
m = Model()


