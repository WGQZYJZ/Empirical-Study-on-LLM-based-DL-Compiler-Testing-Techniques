
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_k, bias=False)  # Initialize a linear layer to apply softmax and then dropout
        self.v = torch.nn.Parameter(torch.randn(d_v, device=device))  # Initialize a parameter with a random standard normal vector
 
    def forward(self, x1):
        k1 = self.qk(x1)  # Compute the dot product of the query and key tensors and store it in k1
        v1 = torch.nn.functional.softmax(k1, dim=-1)  # Apply softmax to the scaled dot product
        qk2 = torch.matmul(v1, self.v)  # Multiply the softmax output by the parameter vector v and then store in qk2
        drop_qk3 = torch.nn.functional.dropout(qk2, p=dropout_p)  # Apply dropout to the multiplied softmax output
        return drop_qk3.matmul(x1)  # Multiply the dropout output by the input tensor x1 and then compute the dot product


# Initializing the model
m = Model()


