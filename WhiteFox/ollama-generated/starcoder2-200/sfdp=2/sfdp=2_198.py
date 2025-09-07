
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, ql=None, k=None, v=None, scale=1e-6):
        query = ql if ql is not None else ql.transpose(-2,-1)

        dot_product = torch.bmm(query, key.transpose(-2, -1)) 
        scaled_dot_product = dot_product / inv_scale_factor
        softmaxed_scaled_dot_product = scaled_dot_product.softmax(dim=-1)

        dropouted_softmaxed_scaled_dot_product = torch.nn.functional.dropout(softmaxed_scaled_dot_product, p=dropout_p)
        output  = dropouted_softmaxed_scaled_dot_product.matmul(value)
        return output

# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(100,512//8) * 3 - 4
key   = torch.randn(64,512//8).transpose(-2,-1) / 5 # Generate a valid key tensor that meets the requirements
value = torch.randn(query.shape[0], query.shape[-1]) # Generate a valid value tensor that meets the requirements. The length of the value should be consistent with the query/key tensor

