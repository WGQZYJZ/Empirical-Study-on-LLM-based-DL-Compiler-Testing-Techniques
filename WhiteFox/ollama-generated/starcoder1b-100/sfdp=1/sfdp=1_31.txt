
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 20, 5))
        self.key   = torch.nn.Parameter(torch.randn(1, 20, 8))
        self.value = torch.nn.Parameter(torch.randn(1, 3, 5, 7))
 
        # Use nn.Linear to convert parameters to their linear representations.
        self.linear_query = torch.nn.Linear(self.query.size()[1], 20)
        self.linear_key   = torch.nn.Linear(self.key.size()[1],  20)
 
    def forward(self, x):
        # Convert query and key to their respective linear representations.
        q = F.linear(x, self.linear_query, self.query)  # Use nn.Linear function to convert a tensor to a feature vector in the space of the linear layer.
 
        k = F.linear(x, self.linear_key,  self.key)   # Use nn.Linear function to convert a tensor to a feature vector in the space of the linear layer.
 
        # Compute a dot product between query and key using torch.matmul.
        qk = q @ k.transpose(-2, -1)  # Use dot product to compute the dot product between the two input tensors (query, key).
        
        # Scale the dot product by an inverse scale factor using torch.div_().
        inv_scale_factor = self.linear_query(self.linear_key)(q.t()).sqrt()
        
        # Apply softmax to the scaled dot product using F.softmax() function, where dim=-1 specifies that softmax should be applied on every element of the second dimension.
        # Softmax is applied in this way because the attention is being applied to a feature vector (not just its features). If the dot product was computed as described above, then softmax would not have been applicable here.
        softmax_qk = F.softmax(qk / inv_scale_factor, dim=-1)
        
        # Apply dropout to the softmax output using dropout_p.
        dropout_qk = nn.functional.dropout(softmax_qk, p=self.p)
 
        # Compute a dot product between dropout output and value tensor using torch.matmul.
        # This is equivalent to computing the sum of squared errors between query and key * value without the square root and then adding 1 after the addition, as explained in Section 4.5 in [Attention Is All You Need].
        output = (dropout_qk @ self.value).view(x.size(0), x.size(2), x.size(3)) + 1
 
        return output


# Initializing the model
m = Model()


