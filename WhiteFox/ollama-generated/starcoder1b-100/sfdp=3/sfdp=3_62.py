
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)
        self.tanh = torch.nn.Tanh()
 
    def forward(self, x1, x2):
        v1  = self.tanh(self.linear(x1))
        v2  = self.tanh(self.linear(x2))
        qk = torch.mm(v1, v2)  # Compute the dot product of the two query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return self.linear(dropout_qk).sigmoid()


# Initializing the model
m  = Model()

