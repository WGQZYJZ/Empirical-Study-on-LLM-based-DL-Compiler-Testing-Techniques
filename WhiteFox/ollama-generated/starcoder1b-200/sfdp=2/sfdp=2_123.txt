
class Model(torch.nn.Module):
    def __init__(self, d_k, nhead):
        super().__init__()
        self.query  = torch.nn.Linear(d_model, d_k)
        self.key    = torch.nn.Linear(d_model, d_k)
        self.value  = torch.nn.Linear(d_model, d_k)

        # Initialize the linear parameters of the two convolution layers.
        for layer in [self.query, self.key]:
            torch.nn.init.xavier_uniform_(layer.weight)
 
        # Initialize the parameter of the output linear layer with
        # `nhead * d_k`.
        self.output = torch.nn.Linear(nhead*d_k, d_model)

        # In order to keep this implementation simple, we assume that
        # d_k = nhead * d_v and we directly set the values of the two
        # linear layers with a uniform distribution. For the more sophisticated
        # Transformer model, we will adjust these parameters based on the input.
        torch.nn.init.xavier_uniform_(self.output.weight)

    def forward(self, x1):
        # The shape of the output matrix is determined by d_k. This matrix stores the product between query and key matrix. In order to keep this model simple, we directly set the values of the two matrices with a uniform distribution, with `nhead * d_k`.
        q  = self.query(x1).reshape(x1.shape[0], -1)  # Query matrix: x1
        k  = self.key(x1).reshape(x1.shape[0], -1)  # Key matrix: x1

        # The shape of the output matrix is determined by nhead * d_k. This matrix stores the product between the two convolution layers. In order to keep this model simple, we directly set the values of the two matrices with a uniform distribution, with `nhead * d_k`.
        v  = self.value(x1).reshape(x1.shape[0], -1)

        q  = torch.nn.functional.dropout(q.mm(k), p=self.dropout_p)
        output = (q * k).softmax(dim=-1).matmul(v)  # Value matrix: x1 * x1 * v
        output = torch.nn.functional.dropout(output, p=self.dropout_p)  # Dropout layer to prevent overfitting
        output = self.output(output.reshape(-1, self.nhead*self.d_k))

        return output


# Initializing the model
m = Model()

