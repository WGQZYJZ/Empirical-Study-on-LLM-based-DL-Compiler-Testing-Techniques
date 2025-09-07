
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 4096)
        self.key = torch.nn.Linear(768, 4096)
        self.value = torch.nn.Linear(4096, 256)
        self.fc1 = torch.nn.Linear(256, 128)
        self.dropout_layer = torch.nn.Dropout(p=0.1)
 
    def forward(self, x1):
        x1 = x1.contiguous() # Contiguous to let pytorch know that the shape of the input is not change
        query = self.query(x1)
        key = self.key(x1)
        value = self.value(x1)
        query_shape = list(query.size()) # Get query size
        del query
        key_shape = list(key.size()) # Get key size
        del key
        assert len(query_shape) == 4, "Error: input tensor must be a 4D Tensor."
        scale_factor = torch.sqrt(torch.tensor(self.scale_factor).view(-1, 1)).view(query_shape)
        query_reshape = query.contiguous().view(query_shape + [1]) # Expand the query to fit in the shape of a 4D Tensor
        scaled_qk = torch.matmul(query_reshape, key_reshape.transpose(-2, -1)) / scale_factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=self.p)
        output = self.dropout_layer(F.matmul(dropout_qk, value))
        return output


# Initializing the model
m = Model()


