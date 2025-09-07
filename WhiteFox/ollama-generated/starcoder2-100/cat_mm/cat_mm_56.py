class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):

        v2 = torch.matmul(input1, input1)

        #  Concatenating the result tensor along dimension -0 (dimension 0 is row). The length of the list depends on the batch size and number of times the concatenation is performed.
        v3 = torch.cat([v2]*batch_size*num_concatenate_operations , dim=0)
        return v3
