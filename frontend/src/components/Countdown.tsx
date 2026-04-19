"use client";
import { CountdownProps } from "@/types/app";
import { useEffect, useState } from "react";

export default function Countdown({ time, passMatchTimeToParent }: CountdownProps) {
	const [countDown, setCountDown] = useState({
		days: 0,
		hours: 0,
		minutes: 0,
		seconds: 0,
	});

	const startCountDown = (countDown: number) => {
		const days = 1000 * 60 * 60 * 24;
		const hours = 1000 * 60 * 60;
		const minutes = 1000 * 60;
		const seconds = 1000;

		setCountDown({
			days: Math.floor(countDown / days),
			hours: Math.floor((countDown % days) / hours),
			minutes: Math.floor((countDown % hours) / minutes),
			seconds: Math.floor((countDown % minutes) / seconds),
		});
	};

	useEffect(() => {
        if(!time) return;
		let first: boolean = true;
		let target: number = 0;

		const t = setInterval(() => {
			// there is no el clasico scheduled right now
			if (time?.length === 0) {
				clearInterval(t);
				return;
			}

			const oneDayInThePast = -86400000;
			const now = new Date();

			if (first) {
				// calculate the date of the scheduled el clasico with the actual year
				const matchTime: string[] = time.replace(" ", "").replace(":", ".").split(".");
				const deadline: Date = new Date(
					now.getFullYear(),
					parseInt(matchTime[1]) - 1,
					parseInt(matchTime[0]),
					parseInt(matchTime[2]),
					parseInt(matchTime[3]),
				);
				const proposedCountDown = deadline.valueOf() - now.valueOf();

				// if the date is in the past but not longer than 24h,
				// lets assume it was played in the last 24h and
				// turn off the countdown until the next run of the crawler
				if (proposedCountDown < 0 && proposedCountDown > oneDayInThePast) {
					clearInterval(t);
					return;
				}
				// if the date suppose to be before yesterday,
				// lets assume the date is for next year
				else if (proposedCountDown < oneDayInThePast) {
					deadline.setFullYear(deadline.getFullYear() + 1);
				}

				passMatchTimeToParent(deadline);
				target = deadline.valueOf();
				first = false;
			}

			// otherwise start the countdown as is
			startCountDown(target - now.valueOf());
		}, 1000);
	}, [time]);

	return (
		<div id="countdown">
			<div className="grid w-full text-center text-white gap-1.25 grid-cols-[repeat(auto-fit,minmax(100px,1fr))] md:grid-cols-[repeat(auto-fit,minmax(150px,1fr))]">
				<div className="cd-cell">
					<div className="w-25 h-25 mx-auto mb-1.25 leading-25 text-[50px] font-bold bg-[#26cdcb] md:w-full text-shadow-[1px_1px_5px_#136d6c]">
						{countDown.days}
					</div>
					<div className="w-25 mx-auto bg-[#26cdcb] uppercase text-[15px] font-bold md:w-full">Dní</div>
				</div>
				<div className="cd-cell">
					<div className="w-25 h-25 mx-auto mb-1.25 leading-25 text-[50px] font-bold bg-[#26cdcb] md:w-full text-shadow-[1px_1px_5px_#136d6c]">
						{countDown.hours}
					</div>
					<div className="w-25 mx-auto bg-[#26cdcb] uppercase text-[15px] font-bold md:w-full">Hodín</div>
				</div>
				<div className="cd-cell">
					<div className="w-25 h-25 mx-auto mb-1.25 leading-25 text-[50px] font-bold bg-[#26cdcb] md:w-full text-shadow-[1px_1px_5px_#136d6c]">
						{countDown.minutes}
					</div>
					<div className="w-25 mx-auto bg-[#26cdcb] uppercase text-[15px] font-bold md:w-full">Minút</div>
				</div>
				<div className="cd-cell">
					<div className="w-25 h-25 mx-auto mb-1.25 leading-25 text-[50px] font-bold bg-[#26cdcb] md:w-full text-shadow-[1px_1px_5px_#136d6c]">
						{countDown.seconds}
					</div>
					<div className="w-25 mx-auto bg-[#26cdcb] uppercase text-[15px] font-bold md:w-full">Sekúnd</div>
				</div>
			</div>
		</div>
	);
}
