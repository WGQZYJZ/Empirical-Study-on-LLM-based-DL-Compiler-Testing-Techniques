
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        k = self.conv(x2).contiguous()
        q = self.fc(x1).contiguous()
        v = self.conv(k).contiguous()
        k = q @ v.transpose(-2, -1) # Compute the dot product of the query and key tensors
        k = k / np.sqrt(self.embed_dim)  # Scale the dot product by a factor
        k = torch.softmax(k, dim=-1) # Apply softmax to the scaled dot product
        k = torch.nn.functional.dropout(k, p=dropout_p) # Apply dropout to the softmax output
        v = torch.matmul(k, x2)  # Compute the dot product of the dropout output and the value tensor
        return v + bias


# Initializing the model
m = Model()


