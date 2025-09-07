
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((10, 2, 4), requires_grad=True))
        self.key = torch.nn.Parameter(torch.randn((10, 2, 4), requires_grad=True))
        self.value = torch.nn.Parameter(torch.randn((10, 3, 4, 5), requires_grad=True))

    def forward(self, x1):
        k = self.key * math.sqrt(self.query.shape[-2]) # Compute the square root of each of the queries
        qk = torch.matmul(x1, k) # Compute the dot product of each of the inputs and their respective square roots
        sqk = qk.div(math.sqrt(self.key.shape[-2])) # Scale the dot product by the inverse square root
        softmax_qk = sqk.softmax(-2)  # Apply the softmax function to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(self.value).tanh()  # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()


