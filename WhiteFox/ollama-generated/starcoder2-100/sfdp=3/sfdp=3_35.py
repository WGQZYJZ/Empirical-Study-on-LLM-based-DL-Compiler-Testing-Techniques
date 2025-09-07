
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(256, 1024)
        self.scaled_qk = scale_factor * self.qk 
        self.softmax_qk = torch.nn.Softmax(-1)(scaled_qk) # Apply softmax to the scaled dot product
        self.dropout_qk = torch.nn.functional.Dropout(p=dropout_p)(softmax_qk, inplace=True)  # Apply dropout to the softmax output
        self.output = torch.nn.Linear(512, num_labels)
 
    def forward(self, query):
        return self.output(self.dropout_qk(self.scaled_qk(query)))


# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(32, 256)

__output__  = m(x1)