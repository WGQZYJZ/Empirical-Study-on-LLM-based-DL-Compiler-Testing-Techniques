
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(4, 10)
        self.key = torch.randn(5, 128)
        self.value = torch.randn(6, 768)

    def forward(self):
        query_key = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk = query_key / math.sqrt(self.key.shape[-1]) 
        softmaxed = torch.nn.functional.softmax(scaled_qk)
        dropouted  = torch.nn.functional.dropout(softmaxed, p=0.75342869)
        return torch.matmul(dropouted, self.value)


# Initializing the model
m  = Model()

# Inputs to the model
query_data = m().detach() # The query tensor
key_data = torch.randn(10) # This is not important since it's being replaced by a fake one.
value_data = torch.randn(768) # This is not important since it's being replaced by a fake one

