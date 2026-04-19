"use client";
import Banner from "./Banner";
import Countdown from "./Countdown";
import { useEffect, useState } from "react";
import { FetchResultSchedule, ScheduleProps } from "@/types/app";

export default function Schedule(props: ScheduleProps) {
	const [matchTime, setMatchTime] = useState<Date>(new Date());
	const [userLanguage, setUserLanguage] = useState<string>("sk-SK");
	const [schedule, setSchedule] = useState<FetchResultSchedule | null>(null);

	useEffect(() => {
		if (typeof navigator !== "undefined" && navigator.language) {
			setUserLanguage(navigator.language);
		}
		if (props.data.length > 0) {
			setSchedule(props.data[0]);
		}
	}, []);

	const getMatchTime = (datetime: Date) => setMatchTime(datetime);

	const formatMatchTime = (matchTime: Date) => {
		const options: Intl.DateTimeFormatOptions = { weekday: "long", year: "numeric", month: "long", day: "numeric" };
		return new Date(matchTime).toLocaleString(userLanguage, options);
	};

	const isClassicoPlanned = (): boolean => !!schedule?.away_team && !!schedule?.home_team && !!schedule?.time;

	const assertName = (team: string): string => (team.includes("Barcelona") ? "Barcelona" : "Real Madrid");

	return (
		schedule && (
			<div id="schedule" className="flex flex-col items-center pt-28 pb-12">
				<div className="container 2xl:w-[60%] 2xl:mx-auto">
					<h1 className="text-center mb-4 text-4xl font-bold tracking-tight text-heading md:text-5xl lg:text-6xl">Nasledujúce El Clasico</h1>
					<h3 className="text-center text-3xl font-bold text-heading">{matchTime instanceof Date ? formatMatchTime(matchTime) : "-"}</h3>
					<Banner
						awayTeam={schedule ? assertName(schedule.away_team) : "-"}
						homeTeam={schedule ? assertName(schedule.home_team) : "-"}
						isPlanned={isClassicoPlanned()}
					/>
					<Countdown time={schedule?.time || ""} passMatchTimeToParent={getMatchTime} />
				</div>
			</div>
		)
	);
}
