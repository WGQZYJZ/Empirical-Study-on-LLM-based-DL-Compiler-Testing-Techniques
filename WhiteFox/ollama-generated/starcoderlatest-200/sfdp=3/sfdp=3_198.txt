
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Conv2d(1, 8, kernel_size=3) # Conv layer for query
        self.k = torch.nn.Conv2d(1, 8, kernel_size=3) # Conv layer for key

    def forward(self, x):
        qv = self.q(x).view(-1, 8, int(x.shape[2]/4), int(x.shape[3]/4))
        kv = self.k(x).view(-1, 8, int(x.shape[2]/4), int(x.shape[3]/4))

        qk = torch.matmul(qv, kv) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        
        output = torch.matmul(dropout_qk, kv).view(-1, 8, int(x.shape[2]/4), int(x.shape[3]/4))
        return output


# Initializing the model
m = Model()
