import tensorflow as tf

# X and Y data
x_train = [1,2,3]
y_train = [1,2,3]

# tf.Variable => trainable variable
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Our hypothesis xW+b
hypopthesis = x_train * W + b

# cost/Loss function
cost = tf.reduce_mean(tf.square(hypopthesis - y_train))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initialize global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
    sess.run(train)
    if (step % 20) == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))