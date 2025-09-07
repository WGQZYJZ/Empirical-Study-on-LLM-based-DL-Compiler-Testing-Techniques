
class Model(torch.nn.Module):
    def __init__(self, head_dim):
        super().__init__()
        self.head_dim = head_dim

        # Use nn.Parameter to create the query and key weights
        self.query_weights  = torch.nn.Parameter(
            data=torch.randn(head_dim, head_dim)
        )
        self.key_weights    = torch.nn.Parameter(
            data=torch.randn(head_dim, head_dim)
        )

        # Use nn.Parameter to create the value and output weights
        self.value_weights  = torch.nn.Parameter(
            data=torch.randn(head_dim, head_dim)
        )

    def forward(self, qk):
        # Compute the dot product of the query and key (qk)
        scaled_qk = torch.matmul(qk, self.query_weights)

        softmax_qk  = scaled_qk.softmax(dim=-1)

        dropout_qk = torch.nn.functional.dropout(
            softmax_qk, p=self.dropout_p
        )

        output      = torch.matmul(dropout_qk, self.value_weights)
        
        return output


# Initializing the model
m = Model(head_dim=1024)

# Inputs to the model
qk = torch.randn(6, 8, 3, 768)
