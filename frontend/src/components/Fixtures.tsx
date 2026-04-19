"use client";
import { FixtureProps, FetchResultFixtures } from "@/types/app";
import { useEffect, useState } from "react";

export default function Fixtures(props: FixtureProps) {
	const [fixtures, setFixtures] = useState<FetchResultFixtures[]>([]);

	useEffect(() => {
		if (props.data.length > 0) {
			setFixtures(props.data);
		}
	}, []);

	const formatMatchTime = (matchDate: string) => {
		return new Date(matchDate).toLocaleDateString(window.navigator.language);
	};

	const getTitle = (event: string, attendance: string) => {
		return attendance.length > 0 ? `Súťaž: ${event}, ${attendance} divákov` : `Súťaž: ${event}`;
	};

	return (
		fixtures?.length > 0 && (
			<div id="fixtures" className="mt-12.5 p-6">
				<h2 className="text-center text-3xl font-bold text-heading mb-8">Hralo sa</h2>

				<div className="timeline grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-5 gap-4 w-full mx-auto text-center my-8">
					{fixtures.map((row, index) => {
						return (
							<a
								key={index}
								title={getTitle(row.event, row.attendance)}
								href={row.link}
								target="_blank"
								rel="noopener noreferrer"
								className="bg-[#24345a] text-white text-center rounded cursor-pointer no-underline
              						h-22.5 leading-5 text-[15px] items-center hover:text-white p-3.75 flex flex-col gap-3"
							>
								<div>
									<span>{formatMatchTime(row.date)}</span>
								</div>
								<div className="grid grid-cols-3 md:text-lg">
									<span className={`${row.home_team == row.winner ? 'font-bold' : ''}`}>{row.home_team}</span>
									<span>{row.score}</span>
									<span className={`${row.away_team == row.winner ? 'font-bold' : ''}`}>{row.away_team}</span>
								</div>
							</a>
						);
					})}
				</div>
			</div>
		)
	);
}
