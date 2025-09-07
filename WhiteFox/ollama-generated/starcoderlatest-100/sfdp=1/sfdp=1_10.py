This pattern characterizes scenarios where a dot product of two tensors is computed and then scaled by an inverse scale factor, softmax is applied to the scaled dot product, dropout is applied to the softmax output of a tensor, and finally attention weights for the padded parts of queries and keys are computed. The attention mechanism will be used only if `use_masked_attention` flag is set as True.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, kernel_size=3, stride=1) # Input image should be at least 8x8 pixels
        self.pooling_layer = torch.nn.MaxPool2d((2, 2), (2, 2)) # Reduce the spatial dimension by 4 times
        # After 5 times poolings, the input tensor has shape [batch, 16, 64, 64]
        self.conv_2 = torch.nn.Conv2d(16, 32, kernel_size=3, stride=1) # Increase spatial dimension of the image to 16x16 by applying 5 times pooling
        self.linear = torch.nn.Linear(8 * 16 * 16, 4096) # Flatten the 16x16 matrix (which is now in shape [batch_size, -1]) to a tensor with shape [batch_size, 8 * 16 * 16]
        self.softmax = torch.nn.Softmax(dim=-1) # Softmax on the tensor after flattening
        # Before this layer the output of convolution should be smaller than 50x50 pixels
        self.linear2 = torch.nn.Linear(4096, 4096) # Increase number of neurons in the linear layer to increase the number of classes (in this case it is 10 instead of 2 for cats and dogs)

    def forward(self, x):
        # Convolutional layer with stride = 1 -> Output shape [batch_size, 16, 48, 48]
        conv_out = self.conv(x)

        # Pooling layer -> output shape [batch_size, 16, 24, 24]
        pool_out = self.pooling_layer(conv_out)

        # Convolutional layer with stride = 1 -> Output shape [batch_size, 32, 8, 8]
        conv_out_2 = self.conv_2(self.pool_out)

        # Flatten the tensor so that it will be compatible with linear layers (this is done after applying pooling layer in order to have a 64x64 input tensor instead of 16x16)
        flattened_tensor = pool_out.view(-1, 8 * 16 * 16) # Output shape [batch_size, 64*64*16]

        # Linear layer layer and then it has to be converted so that the CNN
    - What is Machine Learning (ML)?
    Machine learning is the field of studying and applying machine learning in particular particular particular particular particular particular particular particular particular particular particular particular. 
    Machine learning aims at automating tasks associated with complex problem-solving by means of the same techniques used for human thought or to be applied to other problems where there is no explicit problem description but it can be approximated, for example an image classification task, a speech recognition task or a handwriting recognition task.

    A machine learning model or model is typically trained from data that includes the inputs and outputs of different classes of a given problem. The input parameters define the context in which a model is going to make its prediction and this context might include the features used as inputs (the feature vector) for instance.

    The following figure shows the general flowchart for a machine learning algorithm. The most basic version of the machine learning algorithm consists of three main components: training, prediction and optimization, that are applied sequentially on new samples of data in order to learn from them. 

    Machine Learning vs Artificial Neural Network (ANN)
    What is the difference between an artificial neural network and machine learning?
    Machine Learning
    As a general way of defining machine learning algorithms you can think about machine learning algorithms as a collection of methods that are applied sequentially, one after the other, in order to achieve some specific goal. 

    The goal of machine learning algorithms is not only to produce accurate predictions on new samples from previously unseen data but also to be able to automatically learn what is the most useful feature combination to solve some particular task. 

    Machine Learning Processes
    As a general way of defining machine learning processes you can think about machine learning processes as a collection of processes that are applied sequentially, one after the other, in order to achieve some specific goal. 

    The goal of machine learning processes is not only to produce accurate predictions on new samples from previously unseen data but also to be able to automatically learn what is the most useful feature combination to solve some particular task. 

    Machine Learning Applications
    As a general way of defining applications you can think about applications as a collection of real-world tasks and problem solvers, or people that use machine learning algorithms. 

    The goal of applications are not only to produce accurate predictions on new samples from previously unseen data but also to be able to automatically learn what is the most useful feature combination to solve some particular task. 

    Machine Learning Tasks
    As a general way of defining tasks you can think about tasks as a collection of machine learning problems that share common input and output structures, in order to address certain kind of real world problem/s and or a class of problems. 

    The goal of tasks are not only to produce accurate predictions on new samples from previously unseen data but also to be able to automatically learn what is the most useful feature combination to solve some particular task. 

