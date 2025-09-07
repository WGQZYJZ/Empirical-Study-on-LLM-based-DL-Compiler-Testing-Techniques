
class SelfAttentionModule(torch.nn.Module):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__()
        self.fc = torch.nn.Linear(hidden_dim * 2, hidden_dim)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor=None, dropout_p: float=0.) -> torch.Tensor:
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it by the square root of its size.
        if attn_mask is not None:
            qk += attn_mask
        attn = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        dropout = torch.dropout(attn, dropout_p, True)  # Apply dropout to the softmax output.
        out = dropout @ value  # Compute the dot product of the dropout output and the value.
        out = self.fc(out)
        return out


# Initializing the model with default values
m1  = SelfAttentionModule(hidden_dim=32, dropout_p=0.)
 
 # Inputs to the model
query  = torch.randn(5689, 32),  # The shape of query must be (batch size, hidden dimension).
key  = torch.randn(4718, 32)  # The shape of key should match the shape of value.
value  = torch.randn(4718, 640)

 # Calling the forward pass of the model with default values (with 0. dropout rate and no mask)
out_default  = m1(query=query, key=key, value=value)
 
 
 # Changing values for some of the arguments to produce a new model
m2  = SelfAttentionModule(hidden_dim=64, dropout_p=0.)

 # Inputs to the model after changing some of its inputs. You should expect a different shape (batch size and hidden dimension) from before. Please also check whether the value is sane by comparing the output of this run with that produced earlier.
query  = torch.randn(78, 32),  # The shape of query must be (batch size, hidden dimension). If you provide a different batch size for this input and your model works as expected on previous runs, this may be a hint that you have missed some kind of dropout operation.
key  = torch.randn(154, 32)  # The shape of key should match the shape of value.
value  = torch.randn(78, 640)
 
 ## Now run the forward pass with the new model and new inputs. Do not forget to change some of your input arguments in case you missed some kind of dropout operation earlier.
out_new  = m2(query=query, key=key, value=value)
 
# Please add new arguments that do not require any preprocessing for sanity checks.