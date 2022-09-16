#!/usr/bin/env bash

days=""
for dir in ./$1/*/solutions;
do
	[[ $dir =~ ./$1/(.*)/solutions ]];
	day="${BASH_REMATCH[1]}"

	IFS=", "
	read -ra files <<< "$(ls -A -m $dir)"
	IFS=""
	if [ ${#files[*]} -gt 1 ] || [ ${files[0]} != ".keep" ]
	then
		days="${days}${days:+,}'$day'"
	else
		continue
	fi
done
echo "{'day': [${days}]}"
