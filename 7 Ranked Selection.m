function [index] =  RouletteWheelSelection(arrayInput)
len = length(arrayInput);
% if input is one element then just return rightaway
if len ==1
    index =1;
    return;
end
% normalise inputs to be a well defined distribution
arrayInput = arrayInput/sum(arrayInput);


val = zeros(1,len);
for i=1:len
    val(i) = i;
end
myMap = containers.Map(arrayInput,val);
temp = 0;
cumProb = zeros(1,len);
sort(arrayInput);
for i= 1:len
    cumProb(i) = temp + arrayInput(i);
    temp = cumProb(i);
end
cumProb
i_rand = 0.2;
for i = 1:len
    if i_rand<cumProb(i)
        index = myMap(arrayInput(i));
        return
    end
end
