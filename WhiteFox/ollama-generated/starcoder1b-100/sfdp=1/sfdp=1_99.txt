
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 3)
        self.key = torch.nn.Linear(10, 2)
        self.value = torch.nn.Linear(10, 8)

    def forward(self, x):
        q = self.query(x).view(x.size()[0], -1)  # Convert query into a (batch_size x seq_len) tensor
        k = self.key(x).transpose(1,2)  # Convert key into a (seq_len x batch_size) tensor
        v = self.value(x).view(x.size()[0], -1)  # Convert value into a (batch_size x seq_len) tensor
        dot = torch.matmul(q, k)  # Compute the dot product of query and key tensors
        scaled_dot = dot.div(math.sqrt(float(k.shape[1])))  # Scale the dot product by an inverse scale factor
        softmax_dot = scaled_dot.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_dot = torch.nn.functional.dropout(softmax_dot, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_dot.matmul(v)  # Compute the dot product of the dropout output and value tensor


# Initializing the model
m = Model()


